import google.generativeai as genai, os
import markdown2
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def PMAgent(state):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"You are a PM. Break this down:\n\n{state['input']}")
    text = response.text
    html_output = markdown2.markdown(text)
    return {"__next__": "Architect", "input": html_output, "pm_output": html_output}
