from models.user_model import find_user_by_username, find_user_by_id
from auth_utils import verify_password


def authenticate_user(username, password):
    """Verify credentials and return user data if valid, else None."""
    user = find_user_by_username(username)
    if user is None:
        return None
    if not verify_password(password, user['password_hash']):
        return None
    return dict(user)


def get_current_user(user_id):
    """Return the profile of the currently authenticated user."""
    user = find_user_by_id(user_id)
    return dict(user) if user else None
