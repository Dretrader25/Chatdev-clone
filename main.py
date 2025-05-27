from pm import PMAgent
from architect import ArchitectAgent

# Step 1: Your task for the AI team
task = "Create a platform where users can upload short videos and follow each other."

# Step 2: Project Manager breaks it down
pm_output = PMAgent({"input": task})
print("🧠 PM Agent Response:\n")
print(pm_output)

# Step 3: Architect creates technical plan from PM's breakdown
architect_output = ArchitectAgent(pm_output)
print("\n🏗️ Architect Agent Response:\n")
print(architect_output)
