from flask import request
from src.controller.database.user_controller import Actions
import datetime
action = Actions()

def validate_information(content):

    valids = validate_structure(content=content)
    if valids["valid"] == False:
        return {
            "token":"",
            "wrongData":valids,
            "message":"Algum campo excedeu o limite ou esta formatado erroniamente"
        }

    credentials_validation = action.insert_signin_credentiasl(content=content)

    if credentials_validation == True: message = "Cadastro realizado com sucesso"
    else: message = "Falha ao fazer cadastro, tente novamente"

    return {
        "valid":credentials_validation,
        "redirect":True,
        "message": message
    }

def validate_structure(content):
    retJson ={
        "first_name":(any(not i.isalpha or i !=" " for i in content["first_name"]) and len(content["first_name"]) <= 50),
        "last_name":(any(not i.isalpha or i != " " for i in content["last_name"]) and len(content["last_name"]) <= 50),
        "email":(len(content["email"]) <= 30),
        "nickname":(len(content["nickname"]) <= 16),
        "valid":False
    }
    retJson["valid"] = (
        retJson["first_name"] == True and 
        retJson["last_name"] == True and
        retJson["email"] == True and
        retJson["nickname"] == True
    )
    return retJson
