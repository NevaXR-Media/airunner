# import json
# import os
# from typing import Any, Dict, List

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
# OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaAPI.py")
# ENDPOINT_MAPPING_FILE = os.path.join(BASE_DIR, "endpointMapping.schema.json")

# print(OUTPUT_FILE)
# print(SCHEMA_FILE)

# EndpointMapping = {
#     "Prompts": [
#         {
#             "name": "publicPrompt",
#             "method": "get",
#             "path": "/prompts/:promptId",
#             "type": "Query",
#         },
#         {
#             "name": "publicPrompts",
#             "method": "list",
#             "path": "/prompts",
#             "type": "Query",
#         },
#     ],
#     "Targets": [
#         {
#             "name": "publicTargets",
#             "method": "list",
#             "path": "/targets",
#             "type": "Query",
#         },
#         {
#             "name": "publicTarget",
#             "method": "get",
#             "path": "/targets/:targetId",
#             "type": "Query",
#         },
#     ],
# }


# def load_schema(file_path: str) -> Dict[str, Any]:
#     """Load GraphQL schema from a JSON file."""
#     with open(file_path, "r", encoding="utf-8") as f:
#         return json.load(f)


# def map_graphql_to_python(type_name: str) -> str:
#     """Map GraphQL scalar types to Python types."""
#     mappings = {
#         "Int": "int",
#         "Float": "float",
#         "String": "str",
#         "Boolean": "bool",
#         "ID": "str",
#         "Date": "date",
#         "JSON": "Any",
#     }

#     return mappings.get(type_name, type_name)  # Default to custom type


# def generate_pyi(schema: Dict[str, Any]) -> str:
#     """Generate Python type hints from GraphQL schema."""
#     output = [
#         "from enum import Enum",
#         "from datetime import date",
#         "from typing import TypedDict, Optional, Any, List\n",
#         "from SuperNeva import SNRequest, Auth\n",
#     ]

#     types = schema.get("data", {}).get("__schema", {}).get("types", [])

#     standart_args = "_auth: Optional[Auth] = None"
#     standart_args_pass = f"_auth"

#     import_statements: List[str] = []
#     for endpoint in EndpointMapping:

#         output.append(f"class {endpoint}(SNRequest):")
#         for method in EndpointMapping[endpoint]:

#             graphql_type = next((t for t in types if t["name"] == method["type"]))
#             fields = graphql_type.get("fields", [])
#             field = next((f for f in fields if f["name"] == method["name"]))
#             field_args = field.get("args", [])
#             response_type = field.get("type").get("name")

#             import_statements.append(response_type)

#             print(method["name"], field_args)

#             args: Dict[str, str] = {}
#             for arg in field_args:
#                 if arg["type"]["kind"] == "NON_NULL":
#                     if arg["type"]["kind"] == "LIST":
#                         t = map_graphql_to_python(
#                             arg["type"]["ofType"]["ofType"]["name"]
#                         )
#                         args[arg["name"]] = f'Optional[List["{t}"]]'
#                         if t not in import_statements:
#                             import_statements.append(t)
#                     else:
#                         t = map_graphql_to_python(arg["type"]["ofType"]["name"])
#                         args[arg["name"]] = f'"{t}"'
#                         if t not in import_statements:
#                             import_statements.append(t)
#                 else:
#                     if arg["type"]["kind"] == "LIST":
#                         t = map_graphql_to_python(
#                             arg["type"]["ofType"]["ofType"]["name"]
#                         )
#                         args[arg["name"]] = f'Optional[List["{t}"]]'
#                         if t not in import_statements:
#                             import_statements.append(t)
#                     else:
#                         t = map_graphql_to_python(arg["type"]["name"])
#                         args[arg["name"]] = f'Optional["{t}"]'
#                         if t not in import_statements:
#                             import_statements.append(t)

#             args_str = ", ".join([f"{k}: {v}" for k, v in args.items()])
#             args_keys = ", ".join([f'"{k}": {k}' for k in args.keys()])
#             output.append(
#                 f"    def {method['method']}(self, {args_str}, {standart_args}) -> {response_type}:"
#             )
#             output.append(
#                 f"        return self.request('{method['path']}', body={{{args_keys}}}, {standart_args_pass}) # type: ignore"
#             )
#             output.append("")

#     # Add import statements
#     excluded_imports = {"str", "int", "bool", "date", "Any", "None", ""}
#     for import_statement in import_statements:
#         if import_statement in excluded_imports:
#             continue


#         output.insert(0, f"from SuperNevaTypes import {import_statement}")

#     return "\n".join(output)


# def save_pyi_file(content: str, file_path: str) -> None:
#     """Save generated type hints to a file."""
#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(content)


# if __name__ == "__main__":
#     schema = load_schema(SCHEMA_FILE)
#     pyi_content = generate_pyi(schema)
#     save_pyi_file(pyi_content, OUTPUT_FILE)
#     print(f"Type hints generated in {OUTPUT_FILE}")


# ----------------------------------------------------
# import json
# import os
# from typing import Any, Dict, List, Optional  # type: ignore

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
# OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaAPI.py")
# ENDPOINT_MAPPING_FILE = os.path.join(BASE_DIR, "endpointMapping.schema.json")

# print(OUTPUT_FILE)
# print(SCHEMA_FILE)


# def load_schema(file_path: str) -> Dict[str, Any]:
#     """Load a JSON schema from the specified file."""
#     with open(file_path, "r", encoding="utf-8") as f:
#         return json.load(f)


# def map_graphql_to_python(type_name: str) -> str:
#     """Map GraphQL scalar types to Python native types."""
#     mappings = {
#         "Int": "int",
#         "Float": "float",
#         "String": "str",
#         "Boolean": "bool",
#         "ID": "str",
#         "Date": "date",
#         "JSON": "Any",
#     }
#     return mappings.get(type_name, type_name)  # Default to a custom type


# def generate_pyi(schema: Dict[str, Any]) -> str:
#     """Generate Python type hints from a GraphQL schema."""
#     output = [
#         "from enum import Enum",
#         "from datetime import date",
#         "from typing import TypedDict, Optional, Any, List",
#         "from SuperNeva import SNRequest, Auth",
#         "",  # spacer
#     ]

#     types = schema.get("data", {}).get("__schema", {}).get("types", [])
#     standart_args = "_auth: Optional[Auth] = None"
#     standart_args_pass = "_auth"

#     # This list collects all custom type names to be imported from SuperNevaTypes.
#     import_statements: List[str] = []
#     EndpointMapping = load_schema(ENDPOINT_MAPPING_FILE)

#     # Helper function that derives a Python type annotation from a GraphQL argument.
#     def get_arg_type(arg: Dict[str, Any]) -> str:
#         type_info = arg["type"]
#         if type_info["kind"] == "NON_NULL":
#             inner = type_info["ofType"]
#             if inner["kind"] == "LIST":
#                 t = map_graphql_to_python(inner["ofType"]["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'List["{t}"]'
#             else:
#                 t = map_graphql_to_python(inner["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'"{t}"'
#         else:
#             if type_info["kind"] == "LIST":
#                 t = map_graphql_to_python(type_info["ofType"]["ofType"]["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'Optional[List["{t}"]]'
#             else:
#                 t = map_graphql_to_python(type_info["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'Optional["{t}"]'

#     # Process each endpoint from the mapping.
#     for endpoint, methods in EndpointMapping.items():
#         output.append(f"class {endpoint}(SNRequest):")
#         for method in methods:
#             graphql_type = next((t for t in types if t["name"] == method["type"]), None)
#             if graphql_type is None:
#                 continue

#             fields = graphql_type.get("fields", [])
#             field = next((f for f in fields if f["name"] == method["name"]), None)
#             if field is None:
#                 print(
#                     f"Warning: No field found for method '{method['name']}' in type '{graphql_type.get('name')}'. Skipping."
#                 )
#                 continue

#             field_args = field.get("args", [])
#             response_type = field.get("type", {}).get("name", "Any")
#             if response_type not in import_statements:
#                 import_statements.append(response_type)

#             print(method["name"], field_args)

#             args: Dict[str, str] = {}
#             for arg in field_args:
#                 args[arg["name"]] = get_arg_type(arg)

#             args_str = ", ".join(f"{name}: {typ}" for name, typ in args.items())
#             args_keys = ", ".join(f'"{name}": {name}' for name in args.keys())

#             output.append(
#                 f"    def {method['method']}(self, {args_str}, {standart_args}) -> {response_type}:"
#             )
#             output.append(
#                 f"        return self.request('{method['path']}', body={{{args_keys}}}, {standart_args_pass}) # type: ignore"
#             )
#             output.append("")

#     # Consolidate SuperNevaTypes imports into one multiline statement.
#     excluded = {"str", "int", "bool", "date", "Any", "None", ""}
#     unique_imports = sorted(
#         {imp for imp in import_statements if imp and imp not in excluded}
#     )
#     if unique_imports:
#         multiline_import = (
#             "from SuperNevaTypes import (\n    "
#             + ",\n    ".join(unique_imports)
#             + "\n)"
#         )
#         # Insert after the initial file-level imports.
#         insertion_index = 4  # After "from SuperNeva import SNRequest, Auth"
#         output.insert(insertion_index, multiline_import)

#     return "\n".join(output)


# def save_pyi_file(content: str, file_path: str) -> None:
#     """Save the generated type hints content to the specified file."""
#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(content)


# if __name__ == "__main__":
#     schema = load_schema(SCHEMA_FILE)
#     pyi_content = generate_pyi(schema)
#     save_pyi_file(pyi_content, OUTPUT_FILE)
#     print(f"Type hints generated in {OUTPUT_FILE}")




# ---------------------------------------

# import json
# import os
# from typing import Any, Dict, List, Optional

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
# OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaAPI.py")
# ENDPOINT_MAPPING_FILE = os.path.join(BASE_DIR, "endpointMapping.schema.json")

# print(OUTPUT_FILE)
# print(SCHEMA_FILE)


# def load_schema(file_path: str) -> Dict[str, Any]:
#     """Belirtilen dosyadan JSON şemasını yükler."""
#     with open(file_path, "r", encoding="utf-8") as f:
#         return json.load(f)


# def map_graphql_to_python(type_name: str) -> str:
#     """GraphQL scalar tiplerini Python tiplerine dönüştürür."""
#     mappings = {
#         "Int": "int",
#         "Float": "float",
#         "String": "str",
#         "Boolean": "bool",
#         "ID": "str",
#         "Date": "date",
#         "JSON": "Any",
#     }
#     return mappings.get(type_name, type_name)


# def generate_pyi(schema: Dict[str, Any]) -> str:
#     """
#     GraphQL şemasını ve endpointMapping.json verilerini kullanarak,
#     dinamik ve özyinelemeli (recursive) endpoint sınıflarını içeren tip ipuçları üreten kodu oluşturur.
    
#     Alt endpoint’ler de JSON içindeki yapıya göre sınıf olarak iç içe (nested) eklenir.
#     """
#     output = [
#         "from enum import Enum # type: ignore",
#         "from datetime import date # type: ignore",
#         "from typing import TypedDict, Optional, Any, List # type: ignore",
#         "from SuperNeva import SNRequest, Auth",
#         "",  # spacer
#     ]
    
#     # GraphQL tiplerini şemadan alıyoruz.
#     types = schema.get("data", {}).get("__schema", {}).get("types", [])
#     standart_args = "_auth: Optional[Auth] = None"
#     auth_arg = "_auth"
    
#     # SuperNevaTypes'tan alınacak custom tipleri tutmak için liste
#     import_statements: List[str] = []
    
#     # Endpoint mapping dosyasını yüklüyoruz.
#     EndpointMapping = load_schema(ENDPOINT_MAPPING_FILE)
    
#     def get_arg_type(arg: Dict[str, Any]) -> str:
#         """GraphQL argümanının Python tipini döndürür."""
#         type_info = arg["type"]
#         if type_info["kind"] == "NON_NULL":
#             inner = type_info["ofType"]
#             if inner["kind"] == "LIST":
#                 t = map_graphql_to_python(inner["ofType"]["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'List["{t}"]'
#             else:
#                 t = map_graphql_to_python(inner["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'"{t}"'
#         else:
#             if type_info["kind"] == "LIST":
#                 t = map_graphql_to_python(type_info["ofType"]["ofType"]["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'Optional[List["{t}"]]'
#             else:
#                 t = map_graphql_to_python(type_info["name"])
#                 if t not in import_statements:
#                     import_statements.append(t)
#                 return f'Optional["{t}"]'
    
#     def process_method(method: Dict[str, Any], indent: str = "    ") -> None:
#         """
#         Belirtilen method (endpoint) için fonksiyon imzası oluşturur.
#         GraphQL şemadan argüman tipleri ve dönüş tipi de alınır.
#         """
#         # GraphQL tipini, method'un "type" alanına göre buluyoruz.
#         graphql_type = next((t for t in types if t["name"] == method.get("type", "")), None)
#         if graphql_type is None:
#             print(
#                 f"Warning: GraphQL type '{method.get('type')}' not found for endpoint '{method.get('name')}'. Using default stub."
#             )
#             field_args = []
#             response_type = "Any"
#         else:
#             fields = graphql_type.get("fields", [])
#             field = next((f for f in fields if f["name"] == method.get("name")), None)
#             if field is None:
#                 print(
#                     f"Warning: No field found for method '{method.get('name')}' in type '{graphql_type.get('name')}'. Using default stub."
#                 )
#                 field_args = []
#                 response_type = "Any"
#             else:
#                 field_args = field.get("args", [])
#                 response_type = field.get("type", {}).get("name", "Any")
#         if response_type not in import_statements:
#             import_statements.append(response_type)
    
#         args: Dict[str, str] = {}
#         for arg in field_args:
#             args[arg["name"]] = get_arg_type(arg)
#         args_str = ", ".join(f"{k}: {v}" for k, v in args.items())
#         args_keys = ", ".join(f'"{k}": {k}' for k in args.keys())
    
#         # Fonksiyon ismini URL'den türetiyoruz.
#         path = method.get("path", "")
#         tokens = path.strip("/").split("/")
#         if path.startswith("/accounts/me/"):
#             if tokens and tokens[-1].startswith(":"):
#                 func_name = "get"
#             elif len(tokens) == 3:
#                 func_name = "list"
#             else:
#                 func_name = tokens[-1].lower().replace("-", "_")
#         else:
#             if tokens and tokens[-1].startswith(":"):
#                 func_name = "get"
#             elif len(tokens) == 1:
#                 func_name = "list"
#             else:
#                 func_name = tokens[-1].lower().replace("-", "_")
    
#         if args_str:
#             signature = f"{indent}def {func_name}(self, {args_str}, {standart_args}) -> {response_type}:"
#         else:
#             signature = f"{indent}def {func_name}(self, {standart_args}) -> {response_type}:"
#         output.append(signature)
#         path_value = method.get("path")
#         output.append(
#             f'{indent}    return self.request("{path_value}", body={{{args_keys}}}, {auth_arg})'
#         )
#         output.append("")
    
#     def process_item(item: Any, indent: str = "    ") -> None:
#         """
#         Verilen item; endpoint method mu yoksa alt endpoint grubunu (nested) barındıran sözlük mü
#         onu belirleyip uygun şekilde işleyerek çıktıya ekler.
#         """
#         if isinstance(item, dict):
#             # Eğer "name", "method", "path" ve "type" alanları varsa bu bir endpoint method’dur.
#             if "name" in item and "method" in item and "path" in item and "type" in item:
#                 process_method(item, indent)
#                 # Eğer method'un içinde alt endpoint'ler varsa, method ismini sınıf ismi olarak kullanıp iç sınıf oluşturuyoruz.
#                 if "endpoints" in item and isinstance(item["endpoints"], list) and item["endpoints"]:
#                     nested_class_name = item["name"]
#                     output.append(f"{indent}class {nested_class_name}(SNRequest):")
#                     process_items(item["endpoints"], indent + "    ")
#                     output.append("")
#             else:
#                 # Eğer doğrudan bir endpoint method değilse,
#                 # her anahtarın altındaki listeyi alt sınıf olarak işliyoruz.
#                 for key, value in item.items():
#                     if key == "endpoints" and isinstance(value, list):
#                         # "endpoints" anahtarı sadece liste içeriyorsa doğrudan işleyelim.
#                         process_items(value, indent)
#                     elif isinstance(value, list):
#                         output.append(f"{indent}class {key}(SNRequest):")
#                         process_items(value, indent + "    ")
#                         output.append("")
#         # Eğer item dict değilse, atlıyoruz.
    
#     def process_items(items: List[Any], indent: str = "    ") -> None:
#         """Liste içindeki her bir item için process_item çağırır."""
#         for item in items:
#             process_item(item, indent)
    
#     # Her top-level mapping için; örn. "Prompts", "Targets", "Accounts" vs.
#     for mapping_name, mapping_list in EndpointMapping.items():
#         output.append(f"class {mapping_name}(SNRequest):")
#         process_items(mapping_list, indent="    ")
#         output.append("")
    
#     # SuperNevaTypes'tan alınacak tiplerin tek bir import satırında toplanması.
#     excluded = {"str", "int", "bool", "date", "Any", "None", ""}
#     unique_imports = sorted({imp for imp in import_statements if imp and imp not in excluded})
#     if unique_imports:
#         multiline_import = (
#             "from SuperNevaTypes import (\n    " + ",\n    ".join(unique_imports) + "\n)"
#         )
#         insertion_index = 4
#         output.insert(insertion_index, multiline_import)
    
#     return "\n".join(output)


# def save_pyi_file(content: str, file_path: str) -> None:
#     """Oluşturulan kodu belirtilen dosyaya yazar."""
#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(content)


# if __name__ == "__main__":
#     schema = load_schema(SCHEMA_FILE)
#     pyi_content = generate_pyi(schema)
#     save_pyi_file(pyi_content, OUTPUT_FILE)
#     print(f"Type hints generated in {OUTPUT_FILE}")



import json
import os
from typing import Any, Dict, List, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaAPI.py")
ENDPOINT_MAPPING_FILE = os.path.join(BASE_DIR, "endpointMapping.schema.json")

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
    GraphQL şemasını ve endpointMapping.json verilerini kullanarak,
    dinamik ve özyinelemeli endpoint sınıflarını içeren tip ipuçlarını üreten kodu oluşturur.
    
    Her oluşturulan sınıf için tek seferlik __init__ metodu eklenir ve
    *args ile **kwargs parametrelerine tip ipucu (Any) eklenir.
    """
    output = [
        "from enum import Enum # type: ignore",
        "from datetime import date # type: ignore",
        "from typing import TypedDict, Optional, Any, List # type: ignore",
        "from SuperNeva import SNRequest, Auth",
        "",  # spacer
    ]
    
    # GraphQL tiplerini şemadan alıyoruz.
    types = schema.get("data", {}).get("__schema", {}).get("types", [])
    standart_args = "_auth: Optional[Auth] = None"
    auth_arg = "_auth"
    
    # SuperNevaTypes'tan alınacak custom tipleri tutmak için liste
    import_statements: List[str] = []
    
    # SuperNevaTypes'tan alınacak custom tipleri tutmak için liste
    classes: List[str] = []
    
    # Endpoint mapping dosyasını yüklüyoruz.
    EndpointMapping = load_schema(ENDPOINT_MAPPING_FILE)
    
    def get_arg_type(arg: Dict[str, Any]) -> str:
        """GraphQL argümanının Python tipini döndürür."""
        type_info = arg["type"]
        if type_info["kind"] == "NON_NULL":
            inner = type_info["ofType"]
            if inner["kind"] == "LIST":
                t = map_graphql_to_python(inner["ofType"]["name"])
                if t not in import_statements:
                    import_statements.append(t)
                return f'List["{t}"]'
            else:
                t = map_graphql_to_python(inner["name"])
                if t not in import_statements:
                    import_statements.append(t)
                return f'"{t}"'
        else:
            if type_info["kind"] == "LIST":
                t = map_graphql_to_python(type_info["ofType"]["ofType"]["name"])
                if t not in import_statements:
                    import_statements.append(t)
                return f'Optional[List["{t}"]]'
            else:
                t = map_graphql_to_python(type_info["name"])
                if t not in import_statements:
                    import_statements.append(t)
                return f'Optional["{t}"]'
    
    def process_method(method: Dict[str, Any], indent: str = "    ") -> None:
        """
        Belirtilen method (endpoint) için fonksiyon imzası oluşturur.
        GraphQL şemadan argüman tipleri ve dönüş tipi alınır.
        """
        graphql_type = next(
            (t for t in types if t["name"] == method.get("type", "")), None
        )
        if graphql_type is None:
            print(
                f"Warning: GraphQL type '{method.get('type')}' not found for endpoint '{method.get('name')}'. Using default stub."
            )
            field_args = []
            response_type = "Any"
        else:
            fields = graphql_type.get("fields", [])
            field = next((f for f in fields if f["name"] == method.get("name")), None)
            if field is None:
                print(
                    f"Warning: No field found for method '{method.get('name')}' in type '{graphql_type.get('name')}'. Using default stub."
                )
                field_args = []
                response_type = "Any"
            else:
                field_args = field.get("args", [])
                response_type = field.get("type", {}).get("name", "Any")
        if response_type not in import_statements:
            import_statements.append(response_type)
    
        args: Dict[str, str] = {}
        for arg in field_args:
            args[arg["name"]] = get_arg_type(arg)
        args_str = ", ".join(f"{k}: {v}" for k, v in args.items())
        args_keys = ", ".join(f'"{k}": {k}' for k in args.keys())
    
        # --- Fonksiyon ismini URL'den türetiyoruz ---
        path = method.get("path", "")
        tokens = path.strip("/").split("/")
        if path.startswith("/accounts/me/"):
            if tokens and tokens[-1].startswith(":"):
                func_name = "get"
            elif len(tokens) == 3:
                func_name = "list"
            else:
                func_name = tokens[-1].lower().replace("-", "_")
        else:
            if tokens and tokens[-1].startswith(":"):
                func_name = "get"
            elif len(tokens) == 1:
                func_name = "list"
            else:
                func_name = tokens[-1].lower().replace("-", "_")
        # --------------------------------------------------------------------
    
        if args_str:
            signature = f"{indent}def {func_name}(self, {args_str}, {standart_args}) -> {response_type}:"
        else:
            signature = f"{indent}def {func_name}(self, {standart_args}) -> {response_type}:"
        output.append(signature)
        path_value = method.get("path")
        output.append(
            f'{indent}    return self.request("{path_value}", body={{{args_keys}}}, {auth_arg})  # type: ignore'
        )
        output.append("")
    
    def write_class_header(class_name: str, indent: str) -> None:
        """
        Belirtilen indent ile bir sınıf başlığı oluşturur.
        Her sınıf için yalnızca 1 kez __init__ eklenir.
        """
        output.append(f"{indent}class {class_name}(SNRequest):")
        output.append(f"{indent}    def __init__(self, *args: Any, **kwargs: Any) -> None:")
        output.append(f"{indent}        super().__init__(*args, **kwargs)")
    
    def process_item(item: Any, indent: str = "    ") -> None:
        """
        Verilen item; endpoint method mu yoksa nested endpoint'ler içeren sözlük mü
        onu belirleyip uygun şekilde işleyerek çıktıya ekler.
        """
        if isinstance(item, dict):
            # Eğer "name", "method", "path" ve "type" alanları varsa bu bir endpoint method’dur.
            if "name" in item and "method" in item and "path" in item and "type" in item:
                process_method(item, indent)
                # Eğer method'un içinde alt endpoint'ler varsa, method ismiyle yeni bir sınıf oluşturup işleyelim.
                if "endpoints" in item and isinstance(item["endpoints"], list) and item["endpoints"]:
                    nested_class_name = item["name"]
                    write_class_header(nested_class_name, indent)
                    process_items(item["endpoints"], indent + "    ")
                    output.append("")
            else:
                # Eğer doğrudan bir endpoint method değilse,
                # her anahtarın altındaki listeyi nested sınıf olarak işleyelim.
                for key, value in item.items():
                    if key == "endpoints" and isinstance(value, list):
                        process_items(value, indent)
                    elif isinstance(value, list):
                        write_class_header(key, indent)
                        process_items(value, indent + "    ")
                        output.append("")
    
    def process_items(items: List[Any], indent: str = "    ") -> None:
        """Liste içindeki her bir item için process_item çağırır."""
        for item in items:
            process_item(item, indent)
    
    # Her top-level mapping için; örn. "Prompts", "Targets", "Accounts" vs.
    for mapping_name, mapping_list in EndpointMapping.items():
        # TODO: handle nested endpoints (Get Parent endpoint (key), get current endpoint (key=="method") etc.) > Account + "Me".titlecase() + ...
          
        # TODO: generate classes (Prompts, Targets, Accounts etc.) > generate classes' method's (get,list etc.)
        
        # TODO: generate parent class's __init__ method
      
        
        # write_class_header(mapping_name, "")
        # process_items(mapping_list, indent="    ")
        # output.append("")
    
    # SuperNevaTypes'tan alınacak tipleri tek import satırında toplayalım.
    excluded = {"str", "int", "bool", "date", "Any", "None", ""}
    unique_imports = sorted({imp for imp in import_statements if imp and imp not in excluded})
    if unique_imports:
        multiline_import = (
            "from SuperNevaTypes import (\n    " + ",\n    ".join(unique_imports) + "\n)"
        )
        insertion_index = 4
        output.insert(insertion_index, multiline_import)
    
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

