from sqlalchemy import Column,  BIGINT, Date, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Users(base):
    __tablename__ = "users_info"

    id = Column(BIGINT, primary_key=True, nullable=False)
    first_name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(30), nullable=False)
    password = Column(VARCHAR(16), nullable=False)
    birth_date = Column(Date, nullable=False)

class Hash(base):
    __tablename__ = "hash"

    id = Column(BIGINT, primary_key=True, nullable=False)
    password_hash = Column(VARCHAR(64), nullable=False)
    salt = Column(VARCHAR(32), nullable=False)
    user_id = Column(BIGINT, ForeignKey("users_info.id"), onupdate="CASCADE")