from flask import Flask
from config import setConfigs

app:Flask = setConfigs(Flask(__name__), __name__)

@app.route("/", methods=["GET"])
def main():
    return "main"

if __name__ == "__main__":
    app.run(debug=True)