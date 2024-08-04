from flask import Blueprint, request
from src.models.auth.auth_actions import generate_token

login_bp = Blueprint("login", __name__)
blueprint_url = "/login"
methods = ["POST"]

@login_bp.route(blueprint_url, methods=methods)
def login_method():
    content = request.get_json()
    # go to models and validate informations
    if content["email"] == "email@gmail.com" and content["password"] == "1234":
        # if correts, generate new token in auth and return it
        token = generate_token(content)
        return {
            "token":token,
            "valid":True,
            "message":"Login feito com sucesso, tome o seu token"
        }
    else:
        return {
            "token":"",
            "valid":False,
            "message":"Login não realizado, sem token para você >:("
        }

    # otherwise, else incorrect, return json error without token
    pass