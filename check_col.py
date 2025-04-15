import sqlite3

db_name = "emails.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(emails);")
columns = cursor.fetchall()

ai_response_exists = any(col[1] == "ai_response" for col in columns)

if ai_response_exists:
    print("✅ Column 'ai_response' exists!")
else:
    print("❌ Column 'ai_response' NOT found! Adding it now...")
    cursor.execute("ALTER TABLE emails ADD COLUMN ai_response TEXT;")
    conn.commit()
    print("✅ Column 'ai_response' added successfully!")

conn.close()
