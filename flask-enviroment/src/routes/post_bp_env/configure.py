from flask import Blueprint

post_bp = Blueprint("post", __name__)
blueprint_url = "/make-post"
methods = ["POST"]

@post_bp.route(blueprint_url, methods)
def make_post():
    return