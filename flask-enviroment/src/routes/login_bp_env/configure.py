from flask import Blueprint, request
from src.services.validation.login_validation import validate_information

login_bp = Blueprint("login", __name__)
blueprint_url = "/login"
methods = ["POST"]

@login_bp.route(blueprint_url, methods=methods)
def login_method():
    return validate_information(content=request.get_json())