from src.jwt_initialize import jwt

def setJWT(app):
    jwt.init_app(app=app)

def getJWT():
    return jwt