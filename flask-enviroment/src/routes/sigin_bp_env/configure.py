from flask import Blueprint, request
from src.services.validation.signin_validation import validate_information

signin_bp = Blueprint("signin", __name__)
blueprint_url = "/signin"
methods = ["POST"]

@signin_bp.route(blueprint_url, methods=methods)
def signin_method():
    return validate_information(content=request.get_json())