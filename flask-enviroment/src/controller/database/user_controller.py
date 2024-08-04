from src.controller.database import sessionmaker, sessionObj, select
from src.models.users_model import Users, Hash
from src.services.hash.hash_actions import generate_hash

class Actions:
    def __init__(self):
        self.UsersInstance:Users
        self.HashInstance:Hash

    def validate_login_credentials(self, content):
        self.SetUserInfos(content=content)
        statement = select(self.UsersInstance).where(self.UsersInstance.email == content["email"]).columns()
        passwod = select(self.HashInstance).where(self.Hash.id == statement.column("id")).columns()

        with sessionObj() as session:
            pass

    def insert_signin_credentiasl(self, content):
        # insert all the informations
        self.SetUserInfos(content=content)
        # set up the password hash + saly + cost
        # return the informations less password
        pass

    def SetUserInfos(self, content):
        hashed_password = self.SetHashInfos(content["password"])
        self.UsersInstance = Users(
            first_name=content["first_name"],
            last_name=content["last_name"],
            email=content["email"],
            password=hashed_password,
            birth_date=content["birth_date"]
        )
        
    def SetHashInfos(self,  password, user_id="") -> str:
        gen_password = generate_hash(password, user_id)
        self.SetHashInfos = Hash(
            password_hash=gen_password["hash"],
            salt=gen_password["salt"]
        )
        return gen_password["hash"]
