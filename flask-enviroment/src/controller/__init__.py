from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.enviroment import getElement

engine = create_engine(getElement("SQLALCHEMY_DATABASE_URI"))
session_obj = sessionmaker(bind=engine)