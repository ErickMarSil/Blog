from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

lobby_bp = Blueprint("lobby", __name__)
lobby_bp_url = "/lobby"
methods = ["GET"]

@lobby_bp.route(lobby_bp_url, methods=methods)
@jwt_required()
def lobby():
    user_petname = get_jwt_identity()
    return "Wellcome user" + " " + user_petname["nickname"]