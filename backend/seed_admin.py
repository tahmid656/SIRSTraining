"""
Run this once to create the initial admin user.
Usage: python backend/seed_admin.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from models import get_db
from auth_utils import hash_password

ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@sirs.local'
ADMIN_PASSWORD = 'ChangeMe123!'  # CHANGE THIS after first login


def seed_admin():
    conn = get_db()
    existing = conn.execute(
        'SELECT id FROM users WHERE username = ?', (ADMIN_USERNAME,)
    ).fetchone()

    if existing:
        print(f"Admin user '{ADMIN_USERNAME}' already exists (id={existing['id']}). Skipping.")
        conn.close()
        return

    password_hash = hash_password(ADMIN_PASSWORD)
    conn.execute(
        '''INSERT INTO users (username, email, password_hash, role)
           VALUES (?, ?, ?, ?)''',
        (ADMIN_USERNAME, ADMIN_EMAIL, password_hash, 'admin')
    )
    conn.commit()
    conn.close()
    print(f"Admin user created: username='{ADMIN_USERNAME}', password='{ADMIN_PASSWORD}'")
    print("IMPORTANT: change this password after first login.")


if __name__ == '__main__':
    seed_admin()