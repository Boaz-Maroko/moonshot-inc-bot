import sqlite3

db_path = 'files.db'

def initialize_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userfiles (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   chat_id INTEGER NOT NULL,
                   message_id INTEGER NOT NULL,
                   file_id TEXT NOT NULL
    )
''')
    
    conn.commit()
    conn.close()

def store_files(chat_id, message_id, file_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO userfiles (chat_id, message_id, file_id)
                   VALUES (?, ?, ?)        
    ''', (chat_id, message_id, file_id))
    
    conn.commit()
    conn.close()

initialize_db()
