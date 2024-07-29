from dotenv import load_dotenv
import os

load_dotenv()

def conextion() -> str:
    return os.getenv("DATABASE_URL")

class querys:
    insert_querys = "INSERT INTO users (full_name, email, password, birthdate, nickname) VALUES ('%s', '%s', '%s', DATE '%s', '%s');"
    getter_query = "SELECT * FROM users WHERE users.email = '%s' AND users.password = '%s';"
    remove_query = "DELETE FROM users WHERE users.full_name = '%s';"

    def ret_SIGNIN(
        full_name,
        email,
        password,
        birthdate,
        nickname
    ): return (querys.insert_querys % ("fullname", email, password, birthdate, nickname))
    
    def ret_LOGIN(
        email,
        password
    ): return (querys.getter_query % (email, password))

    def ret_REMOVER(
        fullname
    ): return (querys.remove_query % (fullname))