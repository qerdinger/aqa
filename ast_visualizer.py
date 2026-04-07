import ast
import json

FILENAME = "sample.py"

def serialize(node):
    if isinstance(node, ast.AST):
        return {
            "type": type(node).__name__,
            "fields": {
                k: serialize(v)
                for k, v in ast.iter_fields(node)
            }
        }
    elif isinstance(node, list):
        return [serialize(x) for x in node]
    else:
        return node

code = open(FILENAME).read()
tree = ast.parse(code)

print(json.dumps(serialize(tree), indent=2))