import sqlite3

conn = sqlite3.connect("List.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS List(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    author VARCHAR(50)
)
''')

conn.commit()


def add_users(id, name, author):
    cursor.execute('''
    INSERT INTO users (id, name, author)
    VALUES (?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        author = excluded.age   
''', (id, name, author))
    conn.commit()
