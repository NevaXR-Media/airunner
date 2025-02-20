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


def generate_pyi(schema: Dict[str, Any]) -> str:
    """
    GraphQL şemasını ve endpointMapping.json verilerini kullanarak
    derinlikli (nested) endpoint’leri 'flat' (tek seviyeli) sınıflara dönüştürür.

    - Her node (method veya name) bir path segment’idir.
    - Leaf (endpoints’i olmayan) item’lar o sınıfın metodlarını oluşturur.
    - endpoints alanı varsa, oradan yeni bir path türetilir ve
      yeni bir top-level class yaratılır (nested class yok).

    Not: Derinlik arttığında da bozulmadan çalışır.
    """

    output = [
        "from enum import Enum  # type: ignore",
        "from datetime import date  # type: ignore",
        "from typing import TypedDict, Optional, Any, List  # type: ignore",
        "from SuperNeva import SNRequest, Auth",
        ""
    ]
    
    # GraphQL tiplerini şemadan alıyoruz.
    types = schema.get("data", {}).get("__schema", {}).get("types", [])
    import_statements: List[str] = []
    
    EndpointMapping = load_schema(ENDPOINT_MAPPING_FILE)

    # Bu dict, oluşturulacak sınıfları ve metodlarını tutar.
    # class_registry[class_name] = [ {func_name, path, args, return_type, body_params}, ... ]
    class_registry: Dict[str, List[Dict[str, Any]]] = {}

    # ----------------------------------------------------------------
    #   YARDIMCI FONKSİYONLAR
    # ----------------------------------------------------------------

    def pythonize_path(path_tokens: List[str]) -> str:

        return "".join(seg[0].upper() + seg[1:] for seg in path_tokens if seg)

    def get_field_info(gql_type: str, gql_field_name: str) -> Dict[str, Any]:

        tdef = next((t for t in types if t["name"] == gql_type), None)
        if not tdef:
            return {}
        fields = tdef.get("fields", [])
        return next((f for f in fields if f["name"] == gql_field_name), {})

    def extract_args_and_return(field_info: Dict[str, Any]) -> (List[Dict[str, Any]], str): # type: ignore
        """
        field_info içinden arg listesi ve dönüş tipini al.
        """
        if not field_info:
            return [], "Any"  # type: ignore
        field_args = field_info.get("args", [])
        field_type = field_info.get("type", {})
        ret_type = field_type.get("name", "Any")
        return field_args, ret_type

    def parse_endpoint_item(path_tokens: List[str], item: Dict[str, Any]) -> None:
        """
        Tek bir endpoint item'ını işleyip, class_registry'ye metod olarak ekler.
        item içerisinde "method","name","path","type" varsa -> bu bir leaf endpoint.
        """
        gql_type = item.get("type", "")   # "Query", "Mutation", vb.
        gql_field = item.get("name", "")  # "publicPrompt", "createAccount", vb.

        # GraphQL'de parametre bilgisi arayalım
        field_info = get_field_info(gql_type, gql_field)
        field_args, return_type = extract_args_and_return(field_info)

        if return_type not in ("Any", "") and return_type not in import_statements:
            import_statements.append(return_type)

        # Argüman tiplerini parse edelim
        args_str, args_keys = build_method_args(field_args)  # type: ignore

        # Sınıf adı
        class_name = pythonize_path(path_tokens)

        # Fonksiyon adı (kullanıcı isterse method alanından, isterse name alanından alabilir)
        # Genelde "method" alanı: "list", "get", "create", "update" vs.  
        # "name" alanı: "createAccount", "publicPromptRun" vb.
        # Hangisini fonksiyon ismi yapacağınız size bağlı. Örn. 'method' kullanıyoruz.
        func_name = item["method"]

        # Body
        req_path = item["path"]
        if args_keys.strip():
            req_body = "{" + args_keys + "}"
        else:
            req_body = "{}"

        # Sınıf kaydını oluştur
        if class_name not in class_registry:
            class_registry[class_name] = []
        class_registry[class_name].append({
            "func_name": func_name,
            "return_type": return_type,
            "args_str": args_str,
            "path": req_path,
            "req_body": req_body
        })

    def build_method_args(field_args: List[Dict[str, Any]]) -> (str, str):  # type: ignore

        arg_pairs = []
        arg_body_pairs = []
        for arg in field_args:
            arg_name = arg["name"]
            py_type = map_graphql_arg_type(arg["type"], import_statements)
            arg_pairs.append(f"{arg_name}: {py_type}")
            arg_body_pairs.append(f"\"{arg_name}\": {arg_name}")
        args_str = ", ".join(arg_pairs)
        body_str = ", ".join(arg_body_pairs)
        return args_str, body_str

    def map_graphql_arg_type(type_def: Dict[str, Any], imports: List[str]) -> str:
        """
        NON_NULL, LIST, SCALAR vb. GraphQL tipini Python tipine dönüştürür.
        """
        kind = type_def.get("kind", "")
        if kind == "NON_NULL":
            of_type = type_def.get("ofType", {})
            if of_type.get("kind") == "LIST":
                el_type = map_graphql_to_python(of_type["ofType"]["name"])
                if el_type not in imports:
                    imports.append(el_type)
                return f'List["{el_type}"]'
            else:
                el_type = map_graphql_to_python(of_type.get("name", "Any"))
                if el_type not in imports:
                    imports.append(el_type)
                return f'"{el_type}"'
        elif kind == "LIST":
            # Optional list
            of_type = type_def.get("ofType", {})
            inner_name = of_type.get("ofType", {}).get("name", "Any")
            el_type = map_graphql_to_python(inner_name)
            if el_type not in imports:
                imports.append(el_type)
            return f'Optional[List["{el_type}"]]'
        else:
            # SCALAR veya OBJECT
            el_type = map_graphql_to_python(type_def.get("name", "Any"))
            if el_type not in imports:
                imports.append(el_type)
            return f'Optional["{el_type}"]'

    # ----------------------------------------------------------------
    #   DFS FONKSİYONU - DERİNLİĞİ GEZ
    # ----------------------------------------------------------------

    def dfs(path_tokens: List[str], node: Any) -> None:

        if isinstance(node, dict):
            has_endpoints = "endpoints" in node and isinstance(node["endpoints"], list)
            has_method_and_path = all(k in node for k in ("method", "path", "type", "name"))

            if has_endpoints:
                # Bu node hem bir resource (yeni path segment) hem de alt endpoint’lere sahip olabilir.
                current_method = node.get("method", "")  # path segment
                new_path = path_tokens
                if current_method:
                    new_path = path_tokens + [current_method]

                # Node'un kendisi de endpoint tanımlıyorsa => leaf method olarak ekle
                if has_method_and_path:
                    # Bu node aynı zamanda bir leaf endpoint (mesela "method": "collections" ama kendisi de path’e sahip)
                    # Bunu current sınıfa metod olarak ekle
                    parse_endpoint_item(new_path, node)

                # Şimdi alt endpoints'i gezelim
                for child in node["endpoints"]:
                    dfs(new_path, child)

            else:
                # endpoints yok => bu bir leaf endpoint
                if has_method_and_path:
                    parse_endpoint_item(path_tokens, node)

        elif isinstance(node, list):
            for child in node:
                dfs(path_tokens, child)
        else:
            # int/string vs. atla
            pass

    # ----------------------------------------------------------------
    #  1) TÜM TOP-LEVEL KEY'LERİ (Prompts, Auth, Accounts vb.) DOLAŞ
    # ----------------------------------------------------------------

    for top_key, value in EndpointMapping.items():
        # top_key = "Prompts", "Accounts", ...
        # value -> list
        dfs([top_key], value)

    # ----------------------------------------------------------------
    #  2) Elde ettiğimiz class_registry içindeki veriyi kod olarak yaz
    # ----------------------------------------------------------------

    output.append("")  # Boş satır

    for cls_name, methods in class_registry.items():
        output.append(f"class {cls_name}(SNRequest):")
        # init
        output.append("    def __init__(self, *args: Any, **kwargs: Any) -> None:")
        output.append("        super().__init__(*args, **kwargs)")
        output.append("")

        # Metodları ekleyelim
        for m in methods:
            func_name = m["func_name"]
            ret_type = m["return_type"] if m["return_type"] else "Any"
            args_str = m["args_str"]
            req_path = m["path"]
            req_body = m["req_body"]

            # _auth ekle
            if args_str:
                full_args = f"{args_str}, _auth: Optional[Auth] = None"
            else:
                full_args = "_auth: Optional[Auth] = None"

            output.append(f"    def {func_name}(self, {full_args}) -> {ret_type}:")
            output.append(f"        return self.request(\"{req_path}\", body={req_body}, _auth=_auth)  # type: ignore")
            output.append("")

        output.append("")

    # ----------------------------------------------------------------
    #  3) SuperNevaTypes importlarını ekle
    # ----------------------------------------------------------------

    excluded = {"str", "int", "bool", "date", "Any", "None", ""}
    unique_imports = sorted({imp for imp in import_statements if imp and imp not in excluded})
    if unique_imports:
        multiline_import = (
            "from SuperNevaTypes import (\n    " + ",\n    ".join(unique_imports) + "\n)"
        )
        output.insert(4, multiline_import)

    # Sonuç
    return "\n".join(output)


def save_pyi_file(content: str, file_path: str) -> None:
    """Oluşturulan kodu belirtilen dosyaya yazar."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    schema = load_schema(SCHEMA_FILE)
    pyi_content = generate_pyi(schema)
    save_pyi_file(pyi_content, OUTPUT_FILE)
    print(f"Type hints generated in {OUTPUT_FILE}")
