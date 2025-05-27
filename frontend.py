import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Frontend Developer Agent
def FrontendAgent(architect_output: str):
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    You are the frontend developer for this project.

    Based on the following system architecture from the Software Architect:

    \"\"\"{architect_output}\"\"\"

    Please provide:
    - Which React components should be created
    - A file structure for the frontend
    - Actual React code for at least the main page or login page
    - Be clean, professional, and use Tailwind CSS if appropriate
    """

    response = model.generate_content(prompt)
    return response.text
