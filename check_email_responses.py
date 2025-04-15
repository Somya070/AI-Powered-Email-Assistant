import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("SELECT id, subject, ai_response FROM emails ORDER BY id DESC LIMIT 5")
emails = cursor.fetchall()

for email in emails:
    print(f"📩 ID: {email[0]}")
    print(f"📝 Subject: {email[1]}")
    print(f"🤖 AI Response: {email[2]}\n")

conn.close()

