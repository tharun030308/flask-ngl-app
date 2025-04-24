import sqlite3

con = sqlite3.connect("questions.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col TEXT NOT NULL
)
""")

con.commit()
con.close()
print("Database initialized.")
