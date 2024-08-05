from src.controller.database import sessionmaker, sessionObj, select
from src.models.users_model import Users, Hash
from src.services.hash.hash_actions import generate_hash
from src import db

from sqlalchemy import text

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
        with sessionObj() as session:
            if session.execute(text("SELECT * FROM users_info WHERE email = '%s';" % content["email"])).rowcount > 0: return False

            self.SetUserInfos(content=content)
            session.add(self.UsersInstance)
            self.UsersInstance.password = str(self.SetHashInfos(password=content["password"]))
            session.commit()

    def SetUserInfos(self, content):
        self.UsersInstance = Users(
            first_name=content["first_name"],
            last_name=content["last_name"],
            email=content["email"],
            password=content["password"],
            birth_date=content["birth_date"]
        )
        
    def SetHashInfos(self,  password, user_id, salt="") -> str:
        gen_password = generate_hash(password, salt)
        self.HashInstance = Hash(
            password_hash=gen_password["hash"],
            salt=gen_password["salt"],
            user_id=user_id
        )
        with sessionObj() as session:
            session.add(self.HashInstance)
            session.commit()

        return gen_password["hash"]
