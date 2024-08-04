from flask import jsonify
from src.jwt_initialize.init_jwt import getJWT
from flask_jwt_extended import create_access_token

def generate_token(content):
    jwt = getJWT()
    sendbackJson = {
        "login":content["email"],
        "password":content["password"]
    }
    token = create_access_token(identity=sendbackJson)

    return token

def validate_token(token) -> bool:
    pass