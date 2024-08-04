from hashlib import sha256
import bcrypt

def generate_hash(ori_password, salt=""):
    if salt == "": salt = generate_salt()
    encoded_password = str(ori_password + salt.decode("UTF-8")).encode("UTF-8")
    hash_obj = sha256(encoded_password)
    return {"hash":hash_obj.hexdigest(), "salt":salt}

def generate_salt() -> str:
    return bcrypt.gensalt()