import dotenv
from os import getenv

dotenv.load_dotenv()
def getElement(name):
    return getenv(name)