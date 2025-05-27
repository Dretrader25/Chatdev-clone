import google.generativeai as genai, os
import markdown2
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ArchitectAgent(state):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"You are a software architect. Here's the PM breakdown:\n\n{state['input']}")
    text = response.text
    html_output = markdown2.markdown(text)
    return {"__next__": "Frontend", "input": html_output, "architect_output": html_output}
