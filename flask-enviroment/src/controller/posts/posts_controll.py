from src.models.post_model import Post
from src.controller.posts import session_obj
from sqlalchemy.sql import text
from datetime import datetime

class Actions:
    def __self__ (self):
        self.PostInstance:Post

    def set_infos(self, content):
        self.PostInstance = Post()
        self.PostInstance.nm_title = content["title"]
        self.PostInstance.dt_created = datetime.now()
        self.PostInstance.parent_id = content["parent_id"]

        with session_obj() as session:
            self.PostInstance.id_author = session.execute(
                text(
                    """
                        SELECT id FROM users_info WHERE nick_name = %s;
                    """ % content["author"]
                )
            ).all()[0]

            session.add(instance=self.PostInstance)
            session.commit()
    
    def get_infos(self, content):
        with session_obj() as session:
            query = str(
                """WITH RECURSIVE model AS (
                    SELECT id, title, content
                    FROM posts
                    WHERE id = :id

                    UNION ALL 

                    SELECT p.id, p.title, p.content
                    FROM posts as p
                    JOIN model as m ON p.parent_id = m.id
                    
                )
                SELECT * FROM model;"""
            )
            return session.execute(
                text(query), params={"id":content["id"]}
            ).all()