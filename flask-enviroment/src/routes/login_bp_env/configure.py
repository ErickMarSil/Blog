from flask import Blueprint, request
from src.services.auth.auth_actions import generate_token
from src.controller.database.user_controller import Actions

login_bp = Blueprint("login", __name__)
blueprint_url = "/login"
methods = ["POST"]
action = Actions()

@login_bp.route(blueprint_url, methods=methods)
def login_method():
    content = request.get_json()
    token = ""
    credentials_validation = action.validate_login_credentials(content=content)

    if credentials_validation:
        token = generate_token(content)
        return {
            "token":token,
            "valid":credentials_validation,
            "message":"Login feito com sucesso, tome o seu token"
        }
    else:
        return {
            "token":"",
            "valid":credentials_validation,
            "message":"Login não realizado, sem token para você >:("
        }
        
    # otherwise, else incorrect, return json error without token
    pass