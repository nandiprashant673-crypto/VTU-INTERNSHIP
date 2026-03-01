import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)",
               ("admin", "1234"))

conn.commit()
conn.close()

print("Database Created Successfully!")