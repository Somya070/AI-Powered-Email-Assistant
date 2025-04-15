import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("Loaded API Key:", api_key)

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

# ✅ Configure Gemini model
configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# ✅ Connect to SQLite DB
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# ✅ Fetch emails with missing or placeholder summaries
cursor.execute("""
    SELECT id, subject, body FROM emails 
    WHERE summary IS NULL 
       OR summary IN ('Summary not available', 'No content available to summarize.')
""")
emails = cursor.fetchall()

# ✅ Summarization function
def generate_summary(subject, body):
    prompt = f"""
    Summarize the following email in 1-2 lines:

    Subject: {subject}
    Body: {body}
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"⚠️ Error summarizing email: {e}")
        return "Summary not available"

# ✅ Loop through emails and update summaries
for email in emails:
    email_id, subject, body = email

    if not body or body.strip() == "":
        summary = "No content available to summarize."
    else:
        summary = generate_summary(subject, body)

    print(f"\n📩 ID: {email_id}")
    print(f"📌 Summary: {summary}")

    cursor.execute("UPDATE emails SET summary = ? WHERE id = ?", (summary, email_id))
    conn.commit()

# ✅ Close DB connection
conn.close()
print("\n✅ All summaries generated and saved successfully!")
