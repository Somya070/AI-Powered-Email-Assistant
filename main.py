from email_database import fetch_emails
from chatbot import generate_response, extract_meeting_datetime
from gemini_api import generate_content
from email_utils import is_important_email, summarize_email
from slack_utils import send_slack_message
from calendar_utils import create_calendar_event


def main():
    print("📩 Fetching Emails...")
    email_text = fetch_emails()

    print("🤖 Generating AI Response...")
    ai_response = generate_response(email_text)

    print("\n💡 AI Generated Response:\n")
    print(ai_response)

    # Sample email list — replace this with your real email fetch
    fetched_emails = [
        {
            "subject": "Meeting Request for Friday",
            "body": "Hi Somya, can we have a call on Friday to discuss the project progress?"
        },
        {
            "subject": "50% Off Sale",
            "body": "Check out our biggest discounts of the season!"
        },
    ]

    for email in fetched_emails:
        subject = email['subject']
        body = email['body']

        if is_important_email(subject, body):
            summary = summarize_email(subject, body)
            message = f"📬 *Important Email Alert!*\n*Subject:* {subject}\n*Summary:* {summary}"
            send_slack_message(message)

    summary = generate_content("Summarize this email: Your Netflix account has a new login.")
    print("Gemini Summary:", summary)

    # 🧠 Extract meeting datetime
    sample_meeting_email = "Hi Somya, let's meet on Friday at 3 PM to discuss the project."
    datetime_str = extract_meeting_datetime(sample_meeting_email)
    print("📅 Extracted DateTime:", datetime_str)

    # 📅 Calendar details
    title = "Meeting regarding project progress"
    description = "Discussion on project updates"
    location = "Google Meet"

    # 🗓️ Create calendar event
    from datetime import datetime

    try:
        # Check if the datetime_str is in the right format
        datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

        # ✅ Only if valid, create the event
        create_calendar_event(datetime_str, title, description, location)

    except (ValueError, TypeError):
        print(f"❌ Invalid datetime string: {datetime_str}. Skipping calendar event creation.")


if __name__ == "__main__":
    main()
