import json
import os
from typing import Any, Dict, List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaAPI.py")

print(OUTPUT_FILE)
print(SCHEMA_FILE)

EndpointMapping = {
    "Prompts": [
        {
            "name": "publicPrompt",
            "method": "get",
            "path": "/prompts/:promptId",
            "type": "Query",
        },
        {
            "name": "publicPrompts",
            "method": "list",
            "path": "/prompts",
            "type": "Query",
        },
    ],
    "Targets": [
        {
            "name": "publicTargets",
            "method": "list",
            "path": "/targets",
            "type": "Query",
        },
        {
            "name": "publicTarget",
            "method": "get",
            "path": "/targets/:targetId",
            "type": "Query",
        },
    ],
}


def load_schema(file_path: str) -> Dict[str, Any]:
    """Load GraphQL schema from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def map_graphql_to_python(type_name: str) -> str:
    """Map GraphQL scalar types to Python types."""
    mappings = {
        "Int": "int",
        "Float": "float",
        "String": "str",
        "Boolean": "bool",
        "ID": "str",
        "Date": "date",
        "JSON": "Any",
    }

    return mappings.get(type_name, type_name)  # Default to custom type


def generate_pyi(schema: Dict[str, Any]) -> str:
    """Generate Python type hints from GraphQL schema."""
    output = [
        "from enum import Enum",
        "from datetime import date",
        "from typing import TypedDict, Optional, Any, List\n",
        "from SuperNeva import SNRequest, Auth\n",
    ]

    types = schema.get("data", {}).get("__schema", {}).get("types", [])

    standart_args = "_auth: Optional[Auth] = None"
    standart_args_pass = f"_auth"

    import_statements: List[str] = []
    for endpoint in EndpointMapping:

        output.append(f"class {endpoint}(SNRequest):")
        for method in EndpointMapping[endpoint]:
            print("--------------------------------")
            graphql_type = next((t for t in types if t["name"] == method["type"]))
            fields = graphql_type.get("fields", [])
            field = next((f for f in fields if f["name"] == method["name"]))
            field_args = field.get("args", [])
            response_type = field.get("type").get("name")

            import_statements.append(response_type)

            print(method["name"], field_args)

            args: Dict[str, str] = {}
            for arg in field_args:
                if arg["type"]["kind"] == "NON_NULL":
                    if arg["type"]["kind"] == "LIST":
                        t = map_graphql_to_python(
                            arg["type"]["ofType"]["ofType"]["name"]
                        )
                        args[arg["name"]] = f'Optional[List["{t}"]]'
                        if t not in import_statements:
                            import_statements.append(t)
                    else:
                        t = map_graphql_to_python(arg["type"]["ofType"]["name"])
                        args[arg["name"]] = f'"{t}"'
                        if t not in import_statements:
                            import_statements.append(t)
                else:
                    if arg["type"]["kind"] == "LIST":
                        t = map_graphql_to_python(
                            arg["type"]["ofType"]["ofType"]["name"]
                        )
                        args[arg["name"]] = f'Optional[List["{t}"]]'
                        if t not in import_statements:
                            import_statements.append(t)
                    else:
                        t = map_graphql_to_python(arg["type"]["name"])
                        args[arg["name"]] = f'Optional["{t}"]'
                        if t not in import_statements:
                            import_statements.append(t)

            args_str = ", ".join([f"{k}: {v}" for k, v in args.items()])
            args_keys = ", ".join([f'"{k}": {k}' for k in args.keys()])
            output.append(
                f"    def {method['method']}(self, {args_str}, {standart_args}) -> {response_type}:"
            )
            output.append(
                f"        return self.request('{method['path']}', body={{{args_keys}}}, {standart_args_pass}) # type: ignore"
            )
            output.append("")

    # Add import statements
    for import_statement in import_statements:
        if import_statement == "str":
            continue
        if import_statement == "int":
            continue
        if import_statement == "bool":
            continue
        if import_statement == "date":
            continue
        if import_statement == "Any":
            continue
        if import_statement == "None":
            continue
        if import_statement == "":
            continue
        output.insert(0, f"from SuperNevaTypes import {import_statement}")

    return "\n".join(output)


def save_pyi_file(content: str, file_path: str) -> None:
    """Save generated type hints to a file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    schema = load_schema(SCHEMA_FILE)
    pyi_content = generate_pyi(schema)
    save_pyi_file(pyi_content, OUTPUT_FILE)
    print(f"Type hints generated in {OUTPUT_FILE}")
