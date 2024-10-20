from src.models.post_model import Post
from src.controller.posts import post_session

class Actions:
    def __self__ (self):
        self.PostInstance:Post

    def set_infos(self, content):
        self.PostInstance = Post()
        self.PostInstance.title = content["title"]
        self.PostInstance.content = content["content"]
        self.PostInstance.parent_id = content["parent_id"]

        with post_session() as session:
            session.add(instance=self.PostInstance)
            session.commit()
    
    def get_infos(self, content):
        with post_session() as session:
            query = str(
                """
                WITH RECURSIVE model AS (
                    SELECT id, title, content
                    FROM posts
                    WHERE id = :id

                    UNION ALL 

                    SELECT p.id, p.title, p.content
                    FROM posts as p
                    JOIN model as m ON p.parent_id = m.id
                )
                SELECT * FROM model.
                """
            )
            session.execute(
                query, params={"id":content["id"]}
            )
            pass
        return