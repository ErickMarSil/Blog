from flask import Blueprint

login_bp = Blueprint("login", __name__)
blueprint_url = "/login"
methods = ["POST"]

@login_bp.route(blueprint_url, methods=methods)
def login_method():
    return "login"