from models.incident_model import (
    get_all_incidents,
    get_incidents_by_reporter,
    get_incident_by_id,
    create_incident,
)


def list_all_incidents():
    """Return all incidents. Business logic goes here."""
    # TODO: implement filtering, sorting, pagination
    pass


def list_my_incidents(reporter_id):
    """Return incidents filed by the given user."""
    # TODO: implement filtering, search
    pass


def get_incident_detail(incident_id):
    """Return full detail of a single incident."""
    # TODO: include history/timeline, attachments
    pass


def submit_incident(data):
    """Create a new incident report."""
    # TODO: validate business rules, set initial status, record history
    pass
