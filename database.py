import sqlite3

conn = sqlite3.connect("List.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS List(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    name VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(100),
    sh_desc VARCHAR(100)
)
''')

conn.commit()


def add_list(user_id, name, author, genre):
    cursor.execute('''
    INSERT INTO List (user_id, name, author, genre)
    VALUES (?, ?, ?, ?)
        
''', (user_id, name, author, genre))
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

def find_books(name,author):
    all_lines = cursor.execute('''
        SELECT name, author, sh_desc FROM List 
        WHERE name = ? AND author = ?
    ''', (name,author,))
    return all_lines.fetchall()

