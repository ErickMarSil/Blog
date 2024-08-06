import bcrypt

def generate_hash(ori_password, salt=None):
    if salt == None or salt == "": salt = generate_salt()

    if "bytes" in str(type(salt)):
        pass

    if "bytes" in str(type(ori_password)):
        pass

    hash_obj = bcrypt.hashpw(password=ori_password, salt=salt)
    return {"hash":hash_obj.decode("UTF-8"), "salt":salt.decode("UTF-8")}

def generate_salt() -> str:
    return bcrypt.gensalt(rounds=12)
