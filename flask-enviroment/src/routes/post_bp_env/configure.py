from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.controller.posts.posts_controll import Actions

post_bp = Blueprint("post", __name__)
blueprint_urls = ["/make-post", "/search-post", "/get-post"]
methods = ["POST"]

posts = Actions()

@post_bp.route(blueprint_urls[0],methods=methods)
@jwt_required()
def set_infos():
    return posts.set_infos(request.get_json())

@post_bp.route(blueprint_urls[1], methods=methods)
@jwt_required()
def search_posts():
    return posts.search_posts(request.get_json())

@post_bp.route(blueprint_urls[2], methods=methods)
@jwt_required()
def get_single_post():
    return posts.get_single_post(request.get_json())