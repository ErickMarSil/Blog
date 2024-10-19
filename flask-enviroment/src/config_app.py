from src.enviroment  import getElement

from src import db

from src.routes.login_bp_env.configure import login_bp
from src.routes.sigin_bp_env.configure import signin_bp
from src.routes.lobby_bp_env.configure import lobby_bp

from flask_cors import CORS
from flask import Flask

def setConfigs(app:Flask) -> Flask:
    # set app configurations
    app.config["JWT_SECRET_KEY"] = getElement("FLASK_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = getElement("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_DATABASE_URI_POST"] = getElement("SQLALCHEMY_DATABASE_URI_POST")
    app.config["FLASK_DEBUG"] = getElement("FLASK_DEBUG")
    app.config["FLASK_SQLALCHEMY_ECHO"] = getElement("FLASK_SQLALCHEMY_ECHO")

    # set database configurations
    db.init_app(app)

    # set blueprints for app object
    app.register_blueprint(login_bp)
    app.register_blueprint(signin_bp)
    app.register_blueprint(lobby_bp)

    # set the application as CORS
    CORS(app)

    return app