from flask import jsonify
from models import get_db

def register_routes(app):

    @app.route('/api/incidents', methods=['GET'])
    def list_incidents():
        conn = get_db()
        rows = conn.execute('SELECT * FROM incidents ORDER BY id DESC').fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])

    @app.route('/api/incidents/<int:incident_id>', methods=['GET'])
    def get_incident(incident_id):
        conn = get_db()
        row = conn.execute('SELECT * FROM incidents WHERE id = ?', (incident_id,)).fetchone()
        conn.close()
        if row is None:
            return jsonify({'error': 'Incident not found'}), 404
        return jsonify(dict(row))