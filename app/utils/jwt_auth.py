from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extentions import jwt
from app.models import User

def create_token(user_id):
    return create_access_token(identity=user_id)

def jwt_required_function(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

def get_current_user():
    user_id = get_jwt_identity()
    return User.query.get(user_id)
