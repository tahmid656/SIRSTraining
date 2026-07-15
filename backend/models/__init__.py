import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sirs.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'reporter' CHECK (role IN ('reporter', 'investigator', 'admin')),
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            severity TEXT NOT NULL CHECK (severity IN ('low', 'medium', 'high')),
            description TEXT,
            location TEXT,
            incident_datetime TEXT NOT NULL,
            personnel_involved TEXT,
            status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'in_progress', 'resolved', 'closed')),
            reporter_id INTEGER,
            assigned_to_id INTEGER,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (reporter_id) REFERENCES users(id) ON DELETE SET NULL,
            FOREIGN KEY (assigned_to_id) REFERENCES users(id) ON DELETE SET NULL
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS incident_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            incident_id INTEGER NOT NULL,
            user_id INTEGER,
            action TEXT NOT NULL,
            previous_status TEXT,
            new_status TEXT,
            note TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (incident_id) REFERENCES incidents(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
        )
    ''')

    conn.execute('CREATE INDEX IF NOT EXISTS idx_incidents_reporter ON incidents(reporter_id)')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_incidents_assigned ON incidents(assigned_to_id)')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_incidents_status ON incidents(status)')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_history_incident ON incident_history(incident_id)')

    conn.commit()
    conn.close()
