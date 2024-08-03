from flask import Flask, request

class login:
    app:Flask

    def __init__(self, app):
        login.app = app
        
    def LoginController(self, app:Flask):
        # validate credentials
        # generate jwt if correct
        # send back to server
        pass