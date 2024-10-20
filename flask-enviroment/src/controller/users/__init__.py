from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from src.enviroment import getElement

user_engine = create_engine(getElement("SQLALCHEMY_DATABASE_URI"))
user_session = sessionmaker(bind=user_engine)