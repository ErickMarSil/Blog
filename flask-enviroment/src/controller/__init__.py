from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.enviroment import getElement

engine = create_engine(getElement("SQLALCHEMY_DATABASE_URI"))
session_obj = sessionmaker(bind=engine)
recursive_query = """WITH RECURSIVE model AS (
    SELECT 
        p.id, 
        p.nm_title, 
        p.dt_created,
        p.parent_id
    FROM posts as p
    WHERE p.id = id_code

    UNION ALL 

    SELECT 
        p.id, 
        p.nm_title, 
        p.dt_created,
        p.parent_id
    FROM posts as p
    JOIN model as m ON p.parent_id = m.id
)
SELECT * FROM model;"""