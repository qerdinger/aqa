import ast
import json

FILENAME = "sample.py"

class ASTExtractor:
    def __init__(self, filename: str):
        self.code = open(filename).read()
        self.tree = None
        
    def analyze(self):
        self.tree = ast.parse(self.code)
        return self
    
    def serialize(self):
        return self.Serializable(self.tree)
    
    class Serializable:
        def __init__(self, node):
            self.content = self.inner_rec(node)
        
        def inner_rec(self, node):
            if isinstance(node, ast.AST):
                return {
                    "type": type(node).__name__,
                    "fields": {
                        k: self.inner_rec(v)
                        for k, v in ast.iter_fields(node)
                    }
                }
            elif isinstance(node, list):
                return [self.inner_rec(x) for x in node]
            else:
                return node
        
        def __str__(self):
            return str(self.content)
    
        def as_json(self):
            return json.dumps(self.content, indent=2)


ast_core = ASTExtractor(FILENAME).analyze().serialize()

print(ast_core)
print(ast_core.as_json())