from models import get_db


def find_user_by_username(username):
    """Fetch a user row by username."""
    conn = get_db()
    user = conn.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone()
    conn.close()
    return user


def find_user_by_id(user_id):
    """Fetch a user row by ID (excludes password_hash)."""
    conn = get_db()
    user = conn.execute(
        'SELECT id, username, email, role, created_at FROM users WHERE id = ?',
        (user_id,)
    ).fetchone()
    conn.close()
    return user
