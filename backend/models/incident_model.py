from models import get_db


def get_all_incidents():
    """Fetch all incidents ordered by most recent."""
    conn = get_db()
    rows = conn.execute('SELECT * FROM incidents ORDER BY id DESC').fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_incidents_by_reporter(reporter_id):
    """Fetch incidents filed by a specific user."""
    conn = get_db()
    rows = conn.execute(
        'SELECT * FROM incidents WHERE reporter_id = ? ORDER BY id DESC',
        (reporter_id,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_incident_by_id(incident_id):
    """Fetch a single incident by ID."""
    conn = get_db()
    row = conn.execute(
        'SELECT * FROM incidents WHERE id = ?', (incident_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def create_incident(data):
    """Insert a new incident and return its ID."""
    conn = get_db()
    cursor = conn.execute(
        '''INSERT INTO incidents (title, category, severity, description, location,
           incident_datetime, reporter_id)
           VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (
            data['title'],
            data['category'],
            data['severity'],
            data.get('description'),
            data.get('location'),
            data['incident_datetime'],
            data['reporter_id'],
        )
    )
    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    return incident_id
