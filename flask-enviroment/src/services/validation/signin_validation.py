from flask import request
from src.controller.database.user_controller import Actions
action = Actions()

def validate_information(content):
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

def validate_structure(content):
    retJson ={
        "first_name": (),
        "last_name":()
    }