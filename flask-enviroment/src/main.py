from config import app
from flask import request
from actions.lobby_actions import login_actions, signin_actions

@app.get("/")
def main():
    return "teste"

@app.post("/lobby")
def lobby():
    data = request.get_json()
    if (data["type"] == "login"):
        content = login_actions(data=data)
        return content, 200

    elif (data["type"] == "signin"):
        if(signin_actions(data=data)):
            return "Success"
        else:
            return "Try again"