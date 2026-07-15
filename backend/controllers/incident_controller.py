from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from services.incident_service import (
    list_all_incidents,
    list_my_incidents,
    get_incident_detail,
    submit_incident,
)


@jwt_required()
def get_all_incidents():
    """
    GET /api/incidents
    Security: requires JWT. Only supervisor/admin can see all incidents.
    """
    claims = get_jwt()
    role = claims.get('role')

    if role not in ('investigator', 'admin'):
        return jsonify({'error': 'Forbidden'}), 403

    result = list_all_incidents()
    return jsonify(result)


@jwt_required()
def get_my_incidents():
    """
    GET /api/incidents/mine
    Security: requires JWT. Returns only the caller's incidents.
    """
    user_id = get_jwt_identity()
    result = list_my_incidents(int(user_id))
    return jsonify(result)


@jwt_required()
def get_incident(incident_id):
    """
    GET /api/incidents/<id>
    Security: requires JWT. Reporter can view own; supervisor/admin can view any.
    """
    user_id = get_jwt_identity()
    claims = get_jwt()
    role = claims.get('role')

    incident = get_incident_detail(incident_id)

    if incident is None:
        return jsonify({'error': 'Incident not found'}), 404

    # Access control: reporters can only view their own
    if role == 'reporter' and str(incident.get('reporter_id')) != str(user_id):
        return jsonify({'error': 'Forbidden'}), 403

    return jsonify(incident)


@jwt_required()
def create_incident():
    """
    POST /api/incidents
    Security: requires JWT. Any authenticated user can submit.
    Validation: title, category, severity, and incident_datetime are required.
    """
    user_id = get_jwt_identity()
    data = request.get_json(silent=True) or {}

    # --- Validation ---
    required_fields = ['title', 'category', 'severity', 'incident_datetime']
    missing = [f for f in required_fields if not data.get(f)]
    if missing:
        return jsonify({'error': f'Missing required fields: {", ".join(missing)}'}), 400

    valid_severities = ('low', 'medium', 'high', 'critical')
    if data['severity'] not in valid_severities:
        return jsonify({'error': f'Severity must be one of: {", ".join(valid_severities)}'}), 400

    # --- Attach reporter ---
    data['reporter_id'] = int(user_id)

    # --- Delegate to service ---
    result = submit_incident(data)
    return jsonify(result), 201
