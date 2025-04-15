import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Add summary column if not exists
cursor.execute("PRAGMA table_info(emails);")
columns = cursor.fetchall()

if not any(col[1] == "summary" for col in columns):
    cursor.execute("ALTER TABLE emails ADD COLUMN summary TEXT;")
    conn.commit()
    print("✅ Summary column added!")
else:
    print("✅ Summary column already exists.")

conn.close()
