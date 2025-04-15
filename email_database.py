import sqlite3


def fetch_emails(limit=5):
    """ Fetch latest emails from database """
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT sender, recipient, subject, body FROM emails ORDER BY timestamp DESC LIMIT ?", (limit,))
    emails = cursor.fetchall()

    conn.close()

    # Emails ko formatted text mein convert karna
    email_texts = []
    for email in emails:
        sender, recipient, subject, body = email
        email_text = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
        email_texts.append(email_text)

    return "\n\n---\n\n".join(email_texts)


if __name__ == "__main__":
    print(fetch_emails())  # Testing

def save_ai_response(email_id, ai_response):
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE emails
        SET ai_response = ?
        WHERE id = ?
    ''', (ai_response, email_id))

    conn.commit()
    conn.close()
    print(f"✅ AI response saved for Email ID {email_id}")

    def check_column_exists():
        conn = sqlite3.connect("emails.db")
        cursor = conn.cursor()

        # PRAGMA query to check columns
        cursor.execute("PRAGMA table_info(emails)")
        columns = cursor.fetchall()

        column_names = [col[1] for col in columns]  # Extract column names
        conn.close()

        if "ai_response" in column_names:
            print("✅ `ai_response` column already exists in `emails` table.")
            return True
        else:
            print("❌ `ai_response` column does NOT exist. Adding it now...")
            return False

    # Run the check
    if not check_column_exists():
        conn = sqlite3.connect("emails.db")
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE emails ADD COLUMN ai_response TEXT;")
        conn.commit()
        conn.close()
        print("✅ `ai_response` column added successfully!")

        db_name = "data/emails.db"  # Ensure this path is correct

        def check_table_schema():
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            cursor.execute("PRAGMA table_info(emails);")
            columns = cursor.fetchall()

            for col in columns:
                print(col)

            conn.close()

        # Run this file separately to check table schema
        if __name__ == "__main__":
            check_table_schema()