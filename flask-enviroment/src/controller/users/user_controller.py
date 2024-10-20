from src.controller.users import user_session
from src.models.users_model import Users, Hash
from src.services.hash.hash_actions import generate_hash

from sqlalchemy import text

class Actions:
    def __init__(self):
        self.UsersInstance:Users
        self.HashInstance:Hash

    def validate_login_credentials(self, content):
        # confirm if the email is correct, if so get the user id
        with user_session() as session:
            try:
                user_id = session.execute(text(
                    "SELECT * FROM users_info WHERE email = '%s'" % content["email"]
                )).one()
                hash_password = generate_hash(content["password"].encode("UTF-8"), session.execute(text(
                    "SELECT hash.salt FROM hash WHERE user_id = %s" % user_id[0]
                )).one()[0])["hash"]
            except:
                return {}
            
            if user_id[4] == hash_password:
                return {
                    "name":user_id[1] + " " + user_id[2],
                    "email":user_id[3],
                    "birth_date":user_id[5],
                    "nickname":user_id[6]
                }
            else:
                return {}
                    

    def insert_signin_credentiasl(self, content) -> bool:
        try:
            with sessionObj() as session:
                # check if email already exist
                if session.execute(text(
                    "SELECT * FROM users_info WHERE email = '%s';" % content["email"]
                    )).rowcount > 0: return False

                # create password and set it in the 
                self.SetUserInfos(content=content)
                session.add(self.UsersInstance)
                session.commit()
                session.refresh(self.UsersInstance)

                # generate the hash password
                hashed_password = self.SetHashInfos(password=self.UsersInstance.password)
                session.add(self.HashInstance)
                session.commit()

                # set new hash password to the user
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
    
    def SetHashInfos(self, password, salt="") -> str:
        gen_password = generate_hash((password.encode("UTF-8")), salt)
        self.HashInstance = Hash(
            password_hash=gen_password["hash"],
            salt=gen_password["salt"],
            user_id=self.UsersInstance.id
        )
        
        return gen_password["hash"]
