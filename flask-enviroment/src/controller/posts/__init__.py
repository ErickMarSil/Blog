from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from src.enviroment import getElement

post_engine = create_engine(getElement("SQLALCHEMY_DATABASE_URI_POST"))
post_session = sessionmaker(bind=post_engine)