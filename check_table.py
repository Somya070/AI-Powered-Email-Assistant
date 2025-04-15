import sqlite3

db_name = "emails.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='emails';")
table_exists = cursor.fetchone()

if table_exists:
    print("✅ 'emails' table exists!")
else:
    print("❌ 'emails' table NOT found! You need to create it.")

conn.close()
