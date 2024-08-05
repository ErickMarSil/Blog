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
    credentials_validation = action.insert_signin_credentiasl(content=content)
    if credentials_validation:
        return {
            "valid":True,
            "redirect":{
                "doRedirect":True,
                "routeHttp":"/login"
            },
            "message":"Cadastro feito com sucesso, vá até o login"
        }
    else:
        return {
            "valid":False,
            "redirect":{
                "doRedirect":False,
                "routeHttp":""
            },
            "message":"Cadastro não realizado, tente novamente"
        }
    
    

    # otherwise, else incorrect, return json error without token
    pass