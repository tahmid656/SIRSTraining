from models.incident_model import (
    get_all_incidents,
    get_incidents_by_reporter,
    get_incident_by_id,
    create_incident,
)


def list_all_incidents():
    """Return all incidents."""
    return get_all_incidents()


def list_my_incidents(reporter_id):
    """Return incidents filed by the given user."""
    return get_incidents_by_reporter(reporter_id)


def get_incident_detail(incident_id):
    """Return full detail of a single incident."""
    return get_incident_by_id(incident_id)


def submit_incident(data):
    """Create a new incident report."""
    incident_id = create_incident(data)
    return {'id': incident_id, 'status': 'open', 'message': 'Incident report submitted successfully'}
