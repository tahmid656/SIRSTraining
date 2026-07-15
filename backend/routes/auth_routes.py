from controllers.auth_controller import login, me


def register_auth_routes(app):
    app.add_url_rule('/api/auth/login', view_func=login, methods=['POST'])
    app.add_url_rule('/api/auth/me', view_func=me, methods=['GET'])
