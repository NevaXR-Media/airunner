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
    """Load a JSON schema from the specified file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def map_graphql_to_python(type_name: str) -> str:
    """Map GraphQL scalar types to Python native types."""
    mappings = {
        "Int": "int",
        "Float": "float",
        "String": "str",
        "Boolean": "bool",
        "ID": "str",
        "Date": "date",
        "JSON": "Any",
    }
    return mappings.get(type_name, type_name)  # Default to a custom type


def generate_pyi(schema: Dict[str, Any]) -> str:
    """Generate Python type hints from a GraphQL schema and endpoint mapping.

    For the "accounts" mapping with nested key "me", a nested class structure is generated:
      class accounts(SNRequest):
          def ...  # any top-level endpoints in accounts
          class me:
              class collections(SNRequest):
                  def create(...):
                  def delete(...):
                  ...
              class contents(SNRequest):
                  def get(...):
                  def create(...):
                  ...
              class devices(SNRequest):
                  def list(...):
                  def save(...):
                  ...
    Other mappings are generated as top-level classes.
    The function names are now based solely on the URL:
      - If the URL contains a parameter (":...") then the function name is "get".
      - If the URL is plain (e.g. /accounts/me/states) then the function name is "list".
      - Otherwise, the last token of the URL (lower-cased) is used.
    """
    output = [
        "from enum import Enum # type: ignore",
        "from datetime import date # type: ignore",
        "from typing import TypedDict, Optional, Any, List # type: ignore",
        "from SuperNeva import SNRequest, Auth",
        "",  # spacer
    ]

    # Extract GraphQL types from the schema.
    types = schema.get("data", {}).get("__schema", {}).get("types", [])
    standart_args = "_auth: Optional[Auth] = None"
    auth_arg = "_auth"

    # This list collects all custom type names to be imported from SuperNevaTypes.
    import_statements: List[str] = []

    # Load the endpoint mapping.
    EndpointMapping = load_schema(ENDPOINT_MAPPING_FILE)

    # Helper: Get Python type annotation for a GraphQL argument.
    def get_arg_type(arg: Dict[str, Any]) -> str:
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

    # Helper: Process a single endpoint method using a given indent.
    def process_method(method: Dict[str, Any], indent: str = "    ") -> None:
        # Lookup the GraphQL type based on the method's "type".
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

        # --- New function name logic based solely on the endpoint URL ---
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
            signature = (
                f"{indent}def {func_name}(self, {standart_args}) -> {response_type}:"
            )
        method_body_indent = indent + "    "
        output.append(signature)
        output.append(
            f"{method_body_indent}return self.request('{method.get('path')}', body={{{args_keys}}}, {auth_arg})  # type: ignore"
        )
        output.append("")

    # Helper: Process a list of endpoint methods.
    def process_methods(
        method_entries: List[Dict[str, Any]], indent: str = "    "
    ) -> None:
        for method in method_entries:
            process_method(method, indent)

    # Process each top-level mapping.
    for mapping_name, mapping_list in EndpointMapping.items():
        # Separate direct endpoints and nested mappings.
        top_endpoints = []
        nested_mappings = []  # List of tuples: (nested_key, endpoints_list)
        for item in mapping_list:
            if isinstance(item, dict):
                if "type" in item:
                    top_endpoints.append(item)
                else:
                    for nested_key, endpoints in item.items():
                        nested_mappings.append((nested_key, endpoints))

        # Special handling for "accounts" mapping.
        if mapping_name.lower() == "accounts":
            output.append(f"class {mapping_name}(SNRequest):")
            # Process any top-level endpoints in accounts.
            if top_endpoints:
                process_methods(top_endpoints, indent="    ")
            # Process nested mappings.
            for nested_key, endpoints in nested_mappings:
                # For nested "me", build an inner class with further nested classes.
                if nested_key.lower() == "me":
                    output.append("    class accounts_me:")
                    # Group endpoints by the third token in the URL.
                    groups = {}
                    for endpoint in endpoints:
                        path = endpoint.get("path", "")
                        tokens = path.strip("/").split("/")
                        if len(tokens) >= 3:
                            group_key = tokens[2]
                        else:
                            group_key = "default"
                        groups.setdefault(group_key, []).append(endpoint)
                    for group_key, group_methods in groups.items():
                        output.append(f"        class {group_key}(SNRequest):")
                        process_methods(group_methods, indent="            ")
                        output.append("")
                else:
                    # Other nested mappings under accounts (if any) are generated as inner classes.
                    output.append(f"    class {nested_key}(SNRequest):")
                    process_methods(endpoints, indent="        ")
                    output.append("")
            output.append("")
        else:
            # For non-accounts mappings, generate a top-level class.
            if top_endpoints:
                output.append(f"class {mapping_name}(SNRequest):")
                process_methods(top_endpoints, indent="    ")
                output.append("")
            for nested_key, endpoints in nested_mappings:
                nested_class_name = f"{mapping_name}_{nested_key}"
                output.append(f"class {nested_class_name}(SNRequest):")
                process_methods(endpoints, indent="    ")
                output.append("")

    # Consolidate SuperNevaTypes imports into one multiline statement.
    excluded = {"str", "int", "bool", "date", "Any", "None", ""}
    unique_imports = sorted(
        {imp for imp in import_statements if imp and imp not in excluded}
    )
    if unique_imports:
        multiline_import = (
            "from SuperNevaTypes import (\n    "
            + ",\n    ".join(unique_imports)
            + "\n)"
        )
        # Insert after the file-level imports (after index 4).
        insertion_index = 4
        output.insert(insertion_index, multiline_import)

    return "\n".join(output)


def save_pyi_file(content: str, file_path: str) -> None:
    """Save the generated type hints content to the specified file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    schema = load_schema(SCHEMA_FILE)
    pyi_content = generate_pyi(schema)
    save_pyi_file(pyi_content, OUTPUT_FILE)
    print(f"Type hints generated in {OUTPUT_FILE}")
