import sqlite3
from datetime import datetime

DB_NAME = "expenses.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT,
        description TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()