import sqlite3

conn = sqlite3.connect("List.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS List(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    author VARCHAR(100),
    user_id integer
)
''')

conn.commit()

def add_list(name, author, user_id):
    cursor.execute('''
    INSERT INTO List (name, author, user_id)
    VALUES (?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        author = excluded.age 
''', (name, author, user_id))
    conn.commit()

def show_db():
    all_lines = cursor.execute('''
        SELECT * FROM List  
    ''')
    return all_lines.fetchall()

def get_user_books(user_id):
    all_lines = cursor.execute('''
        SELECT * FROM List 
        WHERE user_id = ?  
    ''', (user_id,))
    return all_lines.fetchall()