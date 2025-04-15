import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Create emails table with threading support
cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        thread_id TEXT,
        sender TEXT,
        recipient TEXT,
        subject TEXT,
        timestamp TEXT,
        body TEXT
    )
''')

# Create attachments table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attachments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_id INTEGER,
        file_name TEXT,
        file_data BLOB,
        FOREIGN KEY (email_id) REFERENCES emails (id)
    )
''')

conn.commit()
conn.close()

print("✅ Database updated with threading & attachments support!")
