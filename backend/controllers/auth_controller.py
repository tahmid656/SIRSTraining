from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from services.auth_service import authenticate_user, get_current_user


def login():
    """Validate login request and delegate to auth service."""
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')

    # --- Validation ---
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # --- Delegate to service ---
    result = authenticate_user(username, password)

    if result is None:
        return jsonify({'error': 'Invalid username or password'}), 401

    # --- Build token ---
    additional_claims = {'role': result['role'], 'username': result['username']}
    access_token = create_access_token(
        identity=str(result['id']),
        additional_claims=additional_claims,
    )

    return jsonify({
        'access_token': access_token,
        'user': {
            'id': result['id'],
            'username': result['username'],
            'email': result['email'],
            'role': result['role'],
        }
    })


@jwt_required()
def me():
    """Return the currently authenticated user's profile."""
    user_id = get_jwt_identity()
    user = get_current_user(user_id)

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(dict(user))
