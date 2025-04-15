from googleapiclient.discovery import build
from email_auth import authenticate_gmail

def fetch_emails(max_results=5):
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    # Fetch messages from inbox
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No emails found.")
        return

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']

        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        snippet = msg_data.get('snippet', '')

        print(f"From: {sender}")
        print(f"Subject: {subject}")
        print(f"Snippet: {snippet}")
        print("-" * 50)

if __name__ == "__main__":
    fetch_emails()

import sqlite3
import base64
import email
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Load credentials from token.json
creds = Credentials.from_authorized_user_file("token.json")

# Gmail API setup
service = build("gmail", "v1", credentials=creds)


def store_email_in_db(sender, recipient, subject, timestamp, body):
    """Store fetched email into the SQLite database"""
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO emails (sender, recipient, subject, timestamp, body)
        VALUES (?, ?, ?, ?, ?)
    ''', (sender, recipient, subject, timestamp, body))

    conn.commit()
    conn.close()
    print(f"✅ Email from {sender} stored in database.")


def fetch_emails():
    """Fetches emails from Gmail"""
    results = service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()

        headers = msg_data["payload"]["headers"]
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")
        recipient = next((h["value"] for h in headers if h["name"] == "To"), "Unknown")
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        timestamp = msg_data["internalDate"]

        # Decode email body
        body = "No Body"
        if "parts" in msg_data["payload"]:
            for part in msg_data["payload"]["parts"]:
                if part["mimeType"] == "text/plain":
                    body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
                    break

        store_email_in_db(sender, recipient, subject, timestamp, body)  # Save email to DB


# Run the function
fetch_emails()

db_name = "data/emails.db"


