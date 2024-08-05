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
        pass

    def insert_signin_credentiasl(self, content):
        try:
            with sessionObj() as session:
                # check if email already exist
                if session.execute(text("SELECT * FROM users_info WHERE email = '%s';" % content["email"])).rowcount > 0: return False

                # create password and set it in the 
                self.SetUserInfos(content=content)
                session.add(self.UsersInstance)
                session.commit()
                session.refresh(self.UsersInstance)

                # generate the hash password
                hashed_password = self.SetHashInfos(password=self.UsersInstance.password)
                self.UsersInstance.password = hashed_password
                session.add(self.UsersInstance)
                session.commit()

                return True
        except():
            return False
        
    def SetUserInfos(self, content):
        self.UsersInstance = Users(
            first_name=content["first_name"],
            last_name=content["last_name"],
            email=content["email"],
            password=content["password"],
            birth_date=content["birth_date"],
            nickname=content["nickname"]
        )
        
    def SetHashInfos(self,  password, salt="") -> str:
        gen_password = generate_hash(password, salt)
        self.HashInstance = Hash(
            password_hash=gen_password["hash"],
            salt=gen_password["salt"],
            user_id=self.UsersInstance.id
        )
        with sessionObj() as session:
            session.add(self.HashInstance)
            session.commit()

        return gen_password["hash"]
