from flask import Flask
from src.enviroment.environ import getElement

def setConfigs(app:Flask, runner:bool) -> Flask:
    app.config["SECRET_KEY"] = getElement("SECRET_KEY")
    app.config["TESTING"] = runner
    app.config["DEBUG"] = True
    app.config["DATABASE_URL"] = getElement("DATABASE_URL")

    return app