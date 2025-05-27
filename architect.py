import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ArchitectAgent(state):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"You are a software architect. Here's the PM breakdown:\n\n{state['input']}")
    text = response.text
    return {"__next__": "Frontend", "input": text, "architect_output": text}
