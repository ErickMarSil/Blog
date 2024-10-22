from sqlalchemy                 import Column,  BIGINT, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.models.users_model     import Users
from sqlalchemy.orm             import relationship

base = declarative_base()

class Post(base):
    __tablename__ = "posts"

    id = Column(BIGINT, primary_key=True, nullable=False)
    nm_title = Column(VARCHAR(25), nullable=False)
    dt_created = Column(TIMESTAMP, nullable=False)
    parent_id = Column(BIGINT, nullable=False)
    id_author = Column(BIGINT, ForeignKey("users_info.id"))

    user = relationship("Users", backref="posts")
