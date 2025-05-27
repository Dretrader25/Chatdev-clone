from graph import workflow

user_input = "Create a platform where users can upload short videos and follow each other."
result = workflow.invoke({"input": user_input})
state = result.get_state()

print("\n✅ FINAL AGENT OUTPUTS:\n")

def clean(value):
    # Handle escaped characters cleanly
    return value.encode("utf-8").decode("unicode_escape") if isinstance(value, str) else value

for key, value in state.items():
    if key.startswith("__"):  # Skip internal routing keys
        continue
    print(f"\n🔹 {key.upper()}:\n")
    print(clean(value))
