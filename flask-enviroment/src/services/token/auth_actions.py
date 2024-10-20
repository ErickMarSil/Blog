from flask import jsonify
from src.jwt_initialize.JwtObj import getJWT
from src.controller.users.user_controller import Actions
from flask_jwt_extended import create_access_token

def generate_token(content):
    jwt = getJWT()
    token = create_access_token(identity=content)
    return token

def validate_token(token) -> bool:
    pass