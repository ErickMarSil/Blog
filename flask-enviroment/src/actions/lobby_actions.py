from config     import db as connection
from loaders    import querys

def create_cursor(query):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query=query)
            try:
                return cursor.fetchall()[0]
            except:
                return cursor.statusmessage

def login_actions(data):
    result = create_cursor(querys.ret_LOGIN(data["email"], data["password"]))
    return ["Email or password incorrect", result][int(len([]) == 0)]

def signin_actions(data):
    result = create_cursor(
        querys.ret_SIGNIN(
            data["fullname"],
            data["email"],
            data["password"],
            data["birthdate"],
            data["nickname"]
        )
    )
    return "INSERT" in result

print(int(len(["a"]) == 0))