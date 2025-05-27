from langgraph.graph import StateGraph
from pm import PMAgent
from architect import ArchitectAgent
from frontend import FrontendAgent

# 1. Create graph
graph = StateGraph()

# 2. Add nodes
graph.add_node("PM", PMAgent)
graph.add_node("Architect", ArchitectAgent)
graph.add_node("Frontend", FrontendAgent)

# 3. Set entry and edges
graph.set_entry_point("PM")
graph.add_edge("PM", "Architect")
graph.add_edge("Architect", "Frontend")

# 4. Set final node
graph.set_finish_point("Frontend")

# 5. Compile graph
workflow = graph.compile()
