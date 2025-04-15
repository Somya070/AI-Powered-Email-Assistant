
import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")  # Replace with your actual API key

model = genai.GenerativeModel("models/gemini-1.5-flash")


def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini Error:", e)
        return "Error in response"

