from flask import Flask
from src.services.config import setConfigs
from src.jwt_initialize.init_jwt import setJWT

app:Flask = setConfigs(Flask(__name__))
setJWT(app)

@app.route("/", methods=["GET"])
def main():
    return "main"

if __name__ == "__main__":
    app.run(debug=True)