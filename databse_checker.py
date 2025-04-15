import sqlite3

# Database ka naam yahan daal
db_name = "your_database_name.db"

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Table ka schema check karne ki query
cursor.execute("PRAGMA table_info(emails);")
columns = cursor.fetchall()

# Print karne ka tareeka
for col in columns:
    print(col)

conn.close()