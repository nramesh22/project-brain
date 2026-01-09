from qdrant_client import QdrantClient
from openai import OpenAI

client = QdrantClient("localhost", port=6333)
llm = OpenAI()

def embed(text):
    return llm.embeddings.create(model="text-embedding-3-large", input=text).data[0].embedding

def store(file, code):
    vec = embed(code)
    client.upsert(
        collection_name="code",
        points=[{"id": hash(file), "vector": vec, "payload": {"file": file}}]
    )
