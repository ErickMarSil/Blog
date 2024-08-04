from src.models import db

class Bases(db.Model):
    def validate_login_credentials(content):
        # take all the user informations
        # validate password in the hash module
        # if corrects return all the content
        # otherwise return none content
        pass

    def insert_signin_credentiasl(content):
        # insert all the informations
        # set up the password hash + saly + cost
        # return the informations less password
        pass