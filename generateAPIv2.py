#GUNCEL KOD
import json
import os
from typing import Any, Dict, List, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaAPI.py")
ENDPOINT_MAPPING_FILE = os.path.join(BASE_DIR, "endpoints.json")

print(OUTPUT_FILE)
print(SCHEMA_FILE)

def load_schema(file_path: str) -> Dict[str, Any]:
    """Belirtilen dosyadan JSON şemasını yükler."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def map_graphql_to_python(type_name: str) -> str:
    """GraphQL scalar tiplerini Python tiplerine dönüştürür."""
    mappings = {
        "Int": "int",
        "Float": "float",
        "String": "str",
        "Boolean": "bool",
        "ID": "str",
        "Date": "date",
        "JSON": "Any",
    }
    return mappings.get(type_name, type_name)

# ------------------- DATA STRUCTURES -------------------
class EndpointDef:
    """
    Bir endpoint fonksiyonunu temsil eder.
    Ek Özellikler:
      ignore_args (List[str]): Bu parametrenin GraphQL arg'lardan silinmesi istenir.
      body (bool): false ise, request'e body={} gönderilir.
    """
    def __init__(self, name: str, method: str, path: str, gql_type: str,
                 ignore_args: List[str], body: bool):
        self.name = name              # GraphQL field name ("createCollection", vs.)
        self.method = method          # "get","list","create", ...
        self.path = path             # "/accounts/me/collections/:collectionId"
        self.gql_type = gql_type     # "Query","Mutation", ...
        self.ignore_args = ignore_args
        self.no_body = (body is False)  # True => body={} gönder
                                        # (body parametresi "false" ise no_body=True)

class Node:
    """
    Her Node, tek bir sınıfı temsil eder.
    - path_tokens: ['Accounts','me','collections'] => class_name: "AccountsMeCollections"
    - method_name: Ebeveynin ctor'unda self.<method_name> = <class_name>(...) => "collections"
    - endpoints: Bu node'a ait fonksiyon tanımları (EndpointDef listesi)
    - children: Alt Node listesi
    """
    def __init__(self, path_tokens: List[str], method_name: str):
        self.path_tokens = path_tokens
        self.method_name = method_name
        self.class_name = "".join(token.capitalize() for token in path_tokens if token)
        self.endpoints: List[EndpointDef] = []
        self.children: List["Node"] = []

# ------------------- PARSE MAPPING -------------------
def build_tree_from_mapping(mapping: Dict[str, Any]) -> List[Node]:
    """endpointMapping'in top-level key'leri için kök Node'lar oluştur."""
    roots: List[Node] = []
    for top_key, items in mapping.items():
        root_node = Node([top_key], method_name=top_key.lower())
        parse_items(items, root_node)
        roots.append(root_node)
    return roots

def parse_items(items: Any, parent: Node):
    """items genellikle list olur. Her elemanı parse_item'e gönderir."""
    if isinstance(items, list):
        for it in items:
            parse_item(it, parent)
    elif isinstance(items, dict):
        parse_item(items, parent)
    else:
        pass

def parse_item(item: Dict[str, Any], parent: Node):
    """
    Bir item inceler:
      - "method","name","path","type" => endpoint
      - "ignoreArgs", "body" => ek parametreler
      - "endpoints" => alt resource
    """
    has_endpoint_fields = all(k in item for k in ("method","name","path","type"))
    endpoints_data = item.get("endpoints")
    method_val = item.get("method") or ""
    name_val   = item.get("name")   or ""
    path_val   = item.get("path")   or ""
    gql_type   = item.get("type")   or ""

    # ignoreArgs ve body
    ignore_args = item.get("ignoreArgs", [])
    if not isinstance(ignore_args, list):
        ignore_args = []
    body_param = item.get("body", True)  # default True => normal body

    # "pass-through" check:
    if not method_val and not name_val and endpoints_data:
        # sadece alt endpoints var => parent'a ekle
        parse_items(endpoints_data, parent)
        return

    # alt "endpoints" var => child node
    if endpoints_data and isinstance(endpoints_data, list):
        seg = method_val or name_val or "unknown"
        child_node = Node(parent.path_tokens + [seg], method_name=seg)

        # eğer bu item aynı zamanda endpoint parametrelerine de sahipse => ekle
        if has_endpoint_fields:
            ep = EndpointDef(name_val, method_val, path_val, gql_type,
                             ignore_args, body_param is False)
            child_node.endpoints.append(ep)

        parse_items(endpoints_data, child_node)
        parent.children.append(child_node)
    else:
        # leaf endpoint => direkt parent'a ekle
        if has_endpoint_fields:
            ep = EndpointDef(name_val, method_val, path_val, gql_type,
                             ignore_args, body_param is False)
            parent.endpoints.append(ep)

# ------------------- GRAPHQL HELPER -------------------
def get_graphql_field(schema_types: List[Dict[str, Any]], gql_type: str, gql_name: str) -> Dict[str, Any]:
    """GraphQL tip listesi içinde gql_type ("Query","Mutation"), oradaki fields içinde gql_name'i döndür."""
    tdef = next((t for t in schema_types if t["name"] == gql_type), None)
    if not tdef:
        return {}
    fields = tdef.get("fields", [])
    return next((f for f in fields if f["name"] == gql_name), {})

def get_arg_type(arg_def: Dict[str, Any], import_list: List[str]) -> str:
    """GraphQL arg tipini (NON_NULL, LIST, vb.) Python tipine dönüştürür."""
    kind = arg_def.get("kind","")
    if kind == "NON_NULL":
        oftype = arg_def.get("ofType", {})
        if oftype.get("kind") == "LIST":
            el = map_graphql_to_python(oftype["ofType"]["name"])
            if el not in import_list:
                import_list.append(el)
            return f'List["{el}"]'
        else:
            el = map_graphql_to_python(oftype.get("name","Any"))
            if el not in import_list:
                import_list.append(el)
            return f'"{el}"'
    elif kind == "LIST":
        inn = arg_def.get("ofType",{}).get("ofType",{}).get("name","Any")
        el = map_graphql_to_python(inn)
        if el not in import_list:
            import_list.append(el)
        return f'Optional[List["{el}"]]'
    else:
        el = map_graphql_to_python(arg_def.get("name","Any"))
        if el not in import_list:
            import_list.append(el)
        return f'Optional["{el}"]'

# ------------------- PATH & BODY HELPER -------------------
def build_fstring_path(path_str: str, path_params: List[str]) -> str:
    """
    /accounts/me/states/:stateId => f"/accounts/me/states/{stateId}"
    path_params: ["stateId"]

    Birden fazla varsa: /some/:a/plus/:b => f"/some/{a}/plus/{b}"
    """
    new_path = path_str
    # Her :xxx i {xxx}'ye dönüştürelim
    for param in path_params:
        marker = f":{param}"
        new_path = new_path.replace(marker, f"{{{param}}}")
    # Son olarak başına f eklenmesi
    return f'f"{new_path}"'

def extract_path_params(path_str: str) -> List[str]:
    """
    /accounts/me/states/:stateId => ["stateId"]
    /some/:a/plus/:b => ["a","b"]
    Basit bir parse: ':' ile başlayan seg'in geri kalanı
    """
    parts = path_str.split("/")
    params = []
    for seg in parts:
        if seg.startswith(":") and len(seg)>1:
            params.append(seg[1:])  # remove ':'
    return params

# ------------------- CODE GENERATION -------------------
def generate_code(roots: List[Node], schema_types: List[Dict[str, Any]]) -> str:
    """
    BFS sırayla: Node -> class
    Each Node => class <class_name>(SNRequest):
        def __init__(...):
            super().__init__(*args, **kwargs)
            self.<childName> = <childClass>(...)
        def <endpoint_method>(...):
            ...
    """
    from collections import deque

    lines: List[str] = []
    import_types: List[str] = []
    visited = set()
    queue = deque(roots)

    def build_method_args(gql_field: Dict[str, Any],
                          ep: EndpointDef) -> (str, str, List[str]):
        """
        graphQL field args -> Python method param + body key
        ep.ignore_args => bu isimleri atla
        path_params => path'te :xyz varsa, 'xyz' parametresi method imzasına eklenir ama body'ye konulmaz

        Return: (args_str, body_key_str, path_params)
        """
        field_args = gql_field.get("args", [])  # [{"name":..., "type":...}, ...]
        # path param'ları
        path_params = extract_path_params(ep.path)
        path_params_set = set(path_params)  # {"stateId", ...}

        arg_pairs = []
        body_pairs = []
        for arg in field_args:
            arg_name = arg["name"]
            if arg_name in ep.ignore_args:
                # skip
                continue
            pytype = get_arg_type(arg["type"], import_types)

            # eğer bu arg_name path'te :arg_name geçiyorsa => method param'da olacak ama body'ye koyma
            if arg_name in path_params_set:
                # method param'a ekle
                arg_pairs.append(f"{arg_name}: {pytype}")
                # body'de yok
            else:
                # normal param
                arg_pairs.append(f"{arg_name}: {pytype}")
                # body'ye ekle
                body_pairs.append(f"\"{arg_name}\": {arg_name}")

        # method arg string
        args_str = ", ".join(arg_pairs)
        # body param str
        body_str = ", ".join(body_pairs)
        return (args_str, body_str, path_params)

    while queue:
        node = queue.popleft()
        if node.class_name in visited:
            continue
        visited.add(node.class_name)

        for child in node.children:
            queue.append(child)

        # Sınıf başlığı
        lines.append(f"class {node.class_name}(SNRequest):")
        lines.append("    def __init__(self, *args: Any, **kwargs: Any) -> None:")
        lines.append("        super().__init__(*args, **kwargs)")

        # Alt node referansları
        for c in node.children:
            lines.append(f"        self.{c.method_name} = {c.class_name}(*args, **kwargs)")
        lines.append("")

        # Endpoint metodları
        for ep in node.endpoints:
            gql_field = get_graphql_field(schema_types, ep.gql_type, ep.name)
            ret_type = gql_field.get("type",{}).get("name","Any")
            if ret_type and ret_type not in ("Any","") and ret_type not in import_types:
                import_types.append(ret_type)

            # Arg parse
            args_str, body_str, path_params = build_method_args(gql_field, ep) # type: ignore

            # method signature
            if args_str.strip(): # type: ignore
                signature_args = f"{args_str}, _auth: Optional[Auth] = None"
            else:
                signature_args = "_auth: Optional[Auth] = None"

            lines.append(f"    def {ep.method}(self, {signature_args}) -> {ret_type}:")

            # path: fstring'e dönüştür
            if path_params:
                new_path = build_fstring_path(ep.path, path_params) # type: ignore
            else:
                new_path = f"\"{ep.path}\""  # normal string

            # body
            if ep.no_body:
                # body = {}
                lines.append(f"        return self.request({new_path}, body={{}}, _auth=_auth)  # type: ignore")
            else:
                # normal case
                if body_str.strip(): # type: ignore
                    lines.append(f"        return self.request({new_path}, body={{ {body_str} }}, _auth=_auth)  # type: ignore")
                else:
                    lines.append(f"        return self.request({new_path}, body={{}}, _auth=_auth)  # type: ignore")

            lines.append("")
        lines.append("")

    # import SuperNevaTypes
    excluded = {"str","int","bool","date","Any","None",""}
    # unique_imports = sorted(x for x in import_types if x not in excluded)
    unique_imports = sorted(x for x in import_types if x and x not in excluded)

    if unique_imports:
        block = (
            "from SuperNevaTypes import (\n    "
            + ",\n    ".join(unique_imports)
            + "\n)\n"
        )
        lines.insert(0, block)

    return "\n".join(lines)

def generate_pyi(schema: Dict[str, Any]) -> str:
    """
    1) endpointMapping.json'u ağaç (Node) olarak parse eder.
    2) BFS ile Node'lardan Python sınıfları oluşturur.
    3) ignoreArgs, body gibi özel parametreleri destekler:
       - ignoreArgs => GraphQL arg'ları method imzasından & body'den çıkar
       - body=false => body={} (boş)
       - pathParam => :xyz => f"/.../{xyz}"
    """
    header = [
        "from enum import Enum  # type: ignore",
        "from datetime import date  # type: ignore",
        "from typing import TypedDict, Optional, Any, List  # type: ignore",
        "from SuperNeva import SNRequest, Auth",
        ""
    ]
    endpoint_mapping = load_schema(ENDPOINT_MAPPING_FILE)
    roots = build_tree_from_mapping(endpoint_mapping)

    schema_types = schema.get("data", {}).get("__schema", {}).get("types", [])
    body = generate_code(roots, schema_types)
    return "\n".join(header) + "\n" + body

def save_pyi_file(content: str, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    schema_data = load_schema(SCHEMA_FILE)
    pyi_content = generate_pyi(schema_data)
    save_pyi_file(pyi_content, OUTPUT_FILE)
    print(f"Type hints generated in {OUTPUT_FILE}")
