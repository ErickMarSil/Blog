from src.app import app


@app.route("\login", methods=["POST"])
def login_function():
    return "login"