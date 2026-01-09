from qdrant_client import QdrantClient
from graph import driver

q = QdrantClient("localhost", port=6333)

def find_relevant(query):
    # Example: dummy vector query, replace with embedding vector
    hits = q.search("code", query_vector=[0]*1536, limit=5)
    files = [h.payload["file"] for h in hits]

    with driver.session() as s:
        res = s.run("""
        MATCH (f:File)-[:CONTAINS]->(fn)
        WHERE f.name IN $files
        RETURN f.name, collect(fn.name)
        """, files=files)
        return list(res)
