import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

def initialize_database():
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (task_name TEXT, created_at TIMESTAMP, due_date TIMESTAMP)')
    conn.commit()
