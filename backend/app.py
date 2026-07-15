from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from models import init_db
from routes.auth_routes import register_auth_routes
from routes.incident_routes import register_incident_routes

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
CORS(app)

# Register route layers
register_auth_routes(app)
register_incident_routes(app)


@app.route('/')
def home():
    return {'status': 'SIRS backend is running'}


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
