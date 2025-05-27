import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Architect Agent
def ArchitectAgent(pm_output: str):
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    You are the Software Architect for a developer team.

    Based on this project manager's task breakdown:

    \"\"\"{pm_output}\"\"\"

    Design a technical plan for how to implement this system. Specify:
    - Which frontend and backend technologies should be used
    - What major components need to be built (database, UI, API)
    - Data flow or basic architecture ideas
    - Any important technical constraints
    """

    response = model.generate_content(prompt)
    return response.text
