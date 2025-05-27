from graph import workflow

user_input = "Build an AI-based chatbot platform for therapists to manage client communication."

# Run the LangGraph workflow with the user input
result = workflow.invoke({"input": user_input})

# Convert LangGraph state object to a plain dictionary
result_dict = dict(result)

# Print all outputs for debugging
print("\n🧠 Full Output State:\n")
for k, v in result_dict.items():
    print(f"{k}:\n{v}\n")

# Specifically print the frontend response
print("\n💡 Final Frontend Output:\n")
print(result_dict.get("frontend_output", "No frontend output found"))
