import google.generativeai as genai, os
import markdown2
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def FrontendAgent(state):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"You are the frontend dev. Here's the architect's plan:\n\n{state['input']}")
    html_output = markdown2.markdown(response.text)
    return {"frontend_output": html_output}
