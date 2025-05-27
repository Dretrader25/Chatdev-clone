from langgraph.graph import StateGraph
from agents.pm import PMAgent
from agents.architect import ArchitectAgent
from agents.frontend import FrontendAgent

graph = StateGraph()
graph.add_node("PM", PMAgent)
graph.add_node("Architect", ArchitectAgent)
graph.add_node("Frontend", FrontendAgent)

graph.set_entry_point("PM")
graph.set_finish_point("Frontend")

workflow = graph.compile()
