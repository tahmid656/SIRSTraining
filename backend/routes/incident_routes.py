from controllers.incident_controller import (
    get_all_incidents,
    get_my_incidents,
    get_incident,
    create_incident,
)


def register_incident_routes(app):
    app.add_url_rule('/api/incidents', view_func=get_all_incidents, methods=['GET'])
    app.add_url_rule('/api/incidents/mine', view_func=get_my_incidents, methods=['GET'])
    app.add_url_rule('/api/incidents/<int:incident_id>', view_func=get_incident, methods=['GET'])
    app.add_url_rule('/api/incidents', view_func=create_incident, methods=['POST'])
