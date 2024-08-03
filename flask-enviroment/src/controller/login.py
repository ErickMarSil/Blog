from flask import Flask, request

class login:
    app:Flask
    
    def __init__(self, app):
        login.app = app
        
    def LoginController(self, app:Flask):
        # validate credentials
        # generate jwt if correct
        # send back to server
        content = request.get_json()
        if self.ValidateInformations(content=content):
            return self.GenerateToke(content=content)
        else: 
            return

    def ValidateInformations(self, content) -> bool:
        pass

    def GenerateToke(self, content) -> str:
        pass

    def ErrorJson():
        pass