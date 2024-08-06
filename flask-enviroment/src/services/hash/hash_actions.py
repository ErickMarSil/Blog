import bcrypt

def generate_hash(ori_password, salt):
    if len(salt) == 0: salt = bcrypt.gensalt(rounds=12)
    elif "str" in str(type(salt)): salt = bytes(salt.encode("UTF-8"))

    hash_obj = bcrypt.hashpw(password=ori_password, salt=salt)
    return {"hash":hash_obj.decode("UTF-8"), "salt":salt.decode("UTF-8")}