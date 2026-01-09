from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j","password"))

def upsert_file(file):
    with driver.session() as s:
        s.run("MERGE (f:File {name:$n})", n=file)

def upsert_function(file, func):
    with driver.session() as s:
        s.run("""
        MERGE (f:File {name:$f})
        MERGE (fn:Function {name:$fn})
        MERGE (f)-[:CONTAINS]->(fn)
        """, f=file, fn=func)

def add_call(src, dst):
    with driver.session() as s:
        s.run("""
        MATCH (a:Function {name:$a})
        MATCH (b:Function {name:$b})
        MERGE (a)-[:CALLS]->(b)
        """, a=src, b=dst)
