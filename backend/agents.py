from langgraph.graph import StateGraph
from openai import OpenAI

llm = OpenAI()

def planner(state):
    return state

def coder(state):
    r = llm.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role":"user","content":state["prompt"]}]
    )
    state["diff"] = r.choices[0].message.content
    return state

graph = StateGraph(dict)
graph.add_node("planner", planner)
graph.add_node("coder", coder)
graph.add_edge("planner","coder")
graph.set_entry_point("planner")
executor = graph.compile()
