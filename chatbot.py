from gemini_api import generate_content

def generate_response(email_text):
    """Generate a summary or reply for the given email using Gemini API."""
    prompt = f"Summarize these emails:\n\n{email_text}"
    return generate_content(prompt)


if __name__ == "__main__":
    sample_text = "Hello, how are you?"  # Testing
    print(generate_response(sample_text))

from gemini_api import generate_content
from datetime import datetime, timedelta
import dateparser

def extract_meeting_datetime(email_text):
    prompt = (
        f"Extract the meeting date and time from this email: \"{email_text}\".\n"
        f"Give only date and time in format like 'Friday at 3 PM'. "
        f"If year or month is missing, still return the available info."
    )
    response = generate_content(prompt)

    # Parse Gemini output using `dateparser` to get actual datetime
    parsed = dateparser.parse(response, settings={"PREFER_DATES_FROM": "future"})
    if parsed:
        return parsed.strftime("%Y-%m-%d %H:%M")
    else:
        return "❌ Could not parse date/time."
