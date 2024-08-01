import dotenv
import os 

dotenv.load_dotenv()

def getElement(Element) -> vars:
    try: ret = os.getenv("Element")
    except: raise TypeError("Didn´t founded your file")
    
    return ret
