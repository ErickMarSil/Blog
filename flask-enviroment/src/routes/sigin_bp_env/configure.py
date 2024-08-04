from flask import Blueprint, request
from src.services.auth.auth_actions import generate_token
from src.controller.database.user_controller import Actions

signin_bp = Blueprint("signin", __name__)
blueprint_url = "/signin"
methods = ["POST"]
action = Actions()

@signin_bp.route(blueprint_url, methods=methods)
def signin_method():
    content = request.get_json()
    token = ""
    credentials_validation = action.insert_signin_credentiasl(content=content)

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