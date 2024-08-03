from flask import Flask
from src.services.config import setConfigs
from src.controller.login import login

app:Flask = setConfigs(Flask(__name__), __name__)
login_endpoint = login(app)

@app.route("/", methods=["GET"])
def main():
    return "main"

@app.route("/login", methods=["POST"])
def call_login(): 
    return login_endpoint.LoginController(app)

if __name__ == "__main__":
    app.run(debug=True)