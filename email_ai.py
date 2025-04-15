import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Key Set Karna
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_ai_response(email_body):

    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(f"Summarize this email and suggest a professional reply:\n\n{email_body}")

    return response.text
