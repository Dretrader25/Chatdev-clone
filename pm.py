import google.generativeai as genai
import os

def PMAgent(state):
    user_input = state["input"]
    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(f"You are a PM. Break this down: {user_input}")
    text = response.text

    return {
        "__next__": "Architect",  # <== Tells LangGraph what node to run next
        "input": text,
        "pm_output": text
    }
