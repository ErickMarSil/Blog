import bcrypt

def generate_hash(ori_password:str, salt=""):
    if salt == "": salt = generate_salt()

    hash_obj = bcrypt.hashpw(password=ori_password.encode(), salt=salt)
    return {"hash":hash_obj.hexdigest(), "salt":salt}

def generate_salt() -> str:
    return bcrypt.gensalt()