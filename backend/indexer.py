import os
from tree_sitter import Language, Parser
from graph import upsert_file, upsert_function
from embeddings import store

# Tree-sitter setup
PY_LANGUAGE = Language("build/my-languages.so", "python")
parser = Parser()
parser.set_language(PY_LANGUAGE)

def index_repo(root):
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(dirpath, f)
                code = open(path).read()
                upsert_file(path)
                tree = parser.parse(bytes(code, "utf8"))
                for node in tree.root_node.children:
                    if node.type == "function_definition":
                        name_node = node.child_by_field_name("name")
                        if name_node:
                            name = code[name_node.start_byte:name_node.end_byte]
                            upsert_function(path, name)
                store(path, code)
