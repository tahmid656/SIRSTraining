from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from models import get_db
from auth_utils import verify_password


def register_auth_routes(app):

    @app.route('/api/auth/login', methods=['POST'])
    def login():
        data = request.get_json(silent=True) or {}
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        conn = get_db()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        conn.close()

        if user is None or not verify_password(password, user['password_hash']):
            return jsonify({'error': 'Invalid username or password'}), 401

        additional_claims = {'role': user['role'], 'username': user['username']}
        access_token = create_access_token(
            identity=str(user['id']),
            additional_claims=additional_claims
        )

        return jsonify({
            'access_token': access_token,
            'user': {
                'id': user['id'],
                'username': user['username'],
                'email': user['email'],
                'role': user['role']
            }
        })

    @app.route('/api/auth/me', methods=['GET'])
    @jwt_required()
    def me():
        user_id = get_jwt_identity()
        claims = get_jwt()

        conn = get_db()
        user = conn.execute(
            'SELECT id, username, email, role, created_at FROM users WHERE id = ?',
            (user_id,)
        ).fetchone()
        conn.close()

        if user is None:
            return jsonify({'error': 'User not found'}), 404

        return jsonify(dict(user))