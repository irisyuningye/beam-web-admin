from app import app, login_manager, user
from flask_login import UserMixin, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)