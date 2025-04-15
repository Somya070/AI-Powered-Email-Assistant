import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Add a new column 'category' if it doesn't exist
cursor.execute("ALTER TABLE emails ADD COLUMN category TEXT")
conn.commit()
conn.close()

print("✅ 'category' column added successfully.")
