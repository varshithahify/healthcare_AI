import sqlite3

conn = sqlite3.connect("patients.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    bp INTEGER,
    sugar INTEGER
)
''')

conn.commit()
conn.close()

print("Database created successfully!")