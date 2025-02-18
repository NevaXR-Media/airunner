import json
import os
from typing import Any, Dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCHEMA_FILE = os.path.join(BASE_DIR, "graphql.schema.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "AIRunner/SuperNevaTypes.py")

print(OUTPUT_FILE)
print(SCHEMA_FILE)


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
    ]

    types = schema.get("data", {}).get("__schema", {}).get("types", [])

    for gql_type in types:
        kind = gql_type["kind"]
        name = gql_type["name"]

        if kind == "INPUT_OBJECT" and not name.startswith("__"):
            output.append(f"class {name}(TypedDict, total=False):")
            for field in gql_type.get("inputFields", []):
                field_name = field["name"]
                # handle list type
                if field["type"]["kind"] == "LIST":
                    field_type = map_graphql_to_python(field["type"]["ofType"]["name"])
                else:
                    field_type = map_graphql_to_python(field["type"]["name"])
                if field_name == "from":
                    field_name = f"__{field_name}"
                output.append(f'    {field_name}: Optional["{field_type}"]')
            output.append("")

        elif kind == "OBJECT" and not name.startswith("__"):
            if name == "Mutation":
                continue
            if name == "Query":
                continue
            if name == "Subscription":
                continue
            output.append(f"class {name}(TypedDict, total=False):")
            for field in gql_type.get("fields", []):
                field_name = field["name"]
                if field_name == "from":
                    field_name = f"__{field_name}"
                # handle list type
                if field["type"]["kind"] == "LIST":
                    if field["type"]["ofType"]["kind"] == "NON_NULL":
                        field_type = map_graphql_to_python(
                            field["type"]["ofType"]["ofType"]["name"]
                        )
                    else:
                        field_type = map_graphql_to_python(
                            field["type"]["ofType"]["name"]
                        )
                    output.append(f'    {field_name}: Optional[List["{field_type}"]]')
                else:
                    field_type = map_graphql_to_python(field["type"]["name"])
                    output.append(f'    {field_name}: Optional["{field_type}"]')

            output.append("")

        elif kind == "ENUM":
            if name.startswith("__"):
                """Do nothing"""
            else:
                output.append(f"class {name}(str, Enum):")
                for enum_value in gql_type.get("enumValues", []):
                    output.append(f'    {enum_value["name"]} = "{enum_value["name"]}"')
                output.append("")

        elif kind == "SCALAR":
            if name not in ("Int", "Float", "String", "Boolean", "ID"):
                output.append(f"{name} = Any")

        elif kind == "UNION":
            output.append(f"{name} = Any")
            output.append("")

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
