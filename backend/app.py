from fastapi import FastAPI
from indexer import index_repo
from context import find_relevant
from agents import executor
from diff_engine import apply

app = FastAPI()

@app.post("/index")
def index(path:str):
    index_repo(path)
    return {"status":"indexed"}

@app.post("/edit")
def edit(req:dict):
    ctx = find_relevant(req.get("query", ""))
    state = executor.invoke({"prompt": f"{req.get('query')}\nContext:{ctx}"})
    apply(state["diff"])
    return {"status":"updated"}
