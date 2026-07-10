import sqlite3

def init_db():
    conn = sqlite3.connect('task_management.db')
    cursor = conn.cursor()

    # Create Task_Titles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Task_Titles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL
        )
    ''')

    # Create Task_Management table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Task_Management (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT NOT NULL,
            task_title_id INTEGER NOT NULL,
            completed BOOLEAN DEFAULT 0,
            FOREIGN KEY (task_title_id) REFERENCES Task_Titles(id)
        )
    ''')

    # Pre-populate Task_Titles with mock data if it's empty
    cursor.execute('SELECT COUNT(*) FROM Task_Titles')
    if cursor.fetchone()[0] == 0:
        mock_titles = [
            ("Excel Sheet Completion",),
            ("Coding",),
            ("Testing",),
            ("ER Diagram",)
        ]
        cursor.executemany('INSERT INTO Task_Titles (title) VALUES (?)', mock_titles)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
