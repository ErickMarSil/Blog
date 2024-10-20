from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.controller.posts.posts_controll import Actions

post_bp = Blueprint("post", __name__)
blueprint_urls = ["/make-post", "/get-post"]
methods = ["POST"]

posts = Actions()

@post_bp.route(blueprint_urls[0],methods=methods)
# @jwt_required()
def make_post():
    posts.set_infos(request.get_json())
    return "foi!"

@post_bp.route(blueprint_urls[1], methods=methods)
def get_post():
    return posts.get_infos(request.get_json())