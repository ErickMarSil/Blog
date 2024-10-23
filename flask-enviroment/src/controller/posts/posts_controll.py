from src.models.post_model import Post
from src.controller import session_obj
from sqlalchemy.sql import text
from datetime import datetime

class Actions:
    def set_infos(self, content):
        require = ["nm_title", "parent_id", "author"]
        if False in [dep in content for dep in require]:
            return 400

        PostInstance = Post()

        PostInstance.nm_title = content["nm_title"]
        PostInstance.dt_created = datetime.now()
        PostInstance.parent_id = content["parent_id"]
        PostInstance.id_author = content["id_author"]

        with session_obj() as session:
            session.add(instance=PostInstance)
            session.commit()
        return {
            "status":"created",
            "message":"Your post was created successfully!"
        }, 200
    
    def search_posts(self, content):
        with session_obj() as session:
            # query = text("SELECT id, nm_title, dt_created FROM posts WHERE nm_title LIKE '%:title%';")
            # result = session.execute(query, params={"title":content["nm_title"]}).all()
            results = session.query(Post).filter(Post.nm_title.ilike(f'%{content["nm_title"]}%')).all()
            results = [{"id":result.id, "id_author":result.id_author,"nm_title":result.nm_title,"dt_created":result.dt_created} for result in results]
            return{
                "content":results,
                "status":None,
                "message":"%s maches with your search!" % len(results)
            }

        pass

    def get_single_post(self, id):
        with session_obj() as session:
            if id == 0:
                return{
                    "content":None,
                    "status":None,
                    "message":"No post founded in our database!"
                }
            
            query = str(
                """WITH RECURSIVE model AS (
                    SELECT 
                        p.id, 
                        p.nm_title, 
                        p.dt_created,
                        p.parent_id
                    FROM posts as p
                    WHERE p.id = :id

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
            )
            post = session.execute(text(query), params={"id":id["id"]}).all()
            post = [{"id":content.id, "nm_title":content.nm_title, "dt_created":content.dt_created, "parent_id":content.parent_id} for content in post]
            return{
                "content":post,
                "status":"Founded",
                "message":"Successfully getted all content!"
            }