from src.controller.database.user_controller import Actions
from src.services.token.auth_actions import generate_token
action = Actions()

def validate_information(content):
    valids = validate_structure(content=content)
    if valids["valid"] == False:
        return {
            "token":"",
            "wrongData":valids,
            "message":"Algumas informações estão incorretas"
        }

    credentials_validation = action.validate_login_credentials(content=content)

    if len(credentials_validation) > 0:
        token = generate_token(credentials_validation)
        return {
            "token":token,
            "valid":True,
            "message":"Login feito com sucesso, redirecionando"
        }
    else:
        return {
            "token":"",
            "valid":False,
            "message":"Login não realizado, email ou senha incorreto(s)"
        }

def validate_structure(content):
    retJson = {
        "email":bool("email" in content and len(content["email"]) <= 30),
        "password":bool("password" in content and len(content["password"]) <= 64),
        "valid":False 
    }
    retJson["valid"] = bool(retJson["email"] == True and retJson["password"] == True)
    return retJson    