import sqlite3

def fetch_latest_emails():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, subject, ai_response FROM emails ORDER BY id DESC LIMIT 5")  # Last 5 emails
    emails = cursor.fetchall()

    for email in emails:
        print(f"📩 Email ID: {email[0]}")
        print(f"📝 Subject: {email[1]}")
        print(f"🤖 AI Response: {email[2]}\n")

    conn.close()

# Test run
fetch_latest_emails()
