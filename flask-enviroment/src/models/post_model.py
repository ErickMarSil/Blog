from sqlalchemy import Column,  BIGINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Post(base):
    __tablename__ = "posts"

    id = Column(BIGINT, primary_key=True, nullable=False)
    title = Column(VARCHAR, nullable=False)
    content = Column(VARCHAR, nullable=False)
    parent_id = Column(BIGINT, nullable=True)