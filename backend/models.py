import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'sirs.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row # access columns by name, not just index
    return conn

def init_db():
    is_new = not os.path.exists(DB_PATH)
    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'open',
            category TEXT NOT NULL,
            location TEXT,
            description TEXT,
            filed_at TEXT NOT NULL,
            assigned_to TEXT
        )
    ''')
    conn.commit()

    if is_new:
        conn.execute('''
            INSERT INTO incidents (title, severity, status, category, location, description, filed_at, assigned_to)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ('Unauthorized access — Gate 3', 'high', 'open', 'Security Breach',
              'Sector 1', 'Individual attempted entry without credentials.',
              '2026-07-12', 'Col. R. Ashworth'))
        conn.commit()

    conn.close()