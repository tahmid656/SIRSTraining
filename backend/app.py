from flask import Flask
from models import init_db
import routes

app = Flask(__name__)

from flask_cors import CORS
CORS(app)

routes.register_routes(app)

@app.route('/')
def home():
    return {'status': 'SIRS backend is running'}

@app.route('/hi')
def hi():
    return {'message': 'hi is working.'}


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)