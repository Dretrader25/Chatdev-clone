import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def PMAgent(state):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"You are a PM. Break this down:\n\n{state['input']}")
    text = response.text
    return {"__next__": "Architect", "input": text, "pm_output": text}
