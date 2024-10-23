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

    def get_single_post(self, content):
        with session_obj() as session:
            id = session.execute(
                "SELECT id FROM posts WHERE title=:nm_title AND id_author=:id_author", 
                params={
                    "nm_title":content["nm_title"],
                    "id_author":content["id_author"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                }
            ).all()

            if id == None or len(id) == 0:
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
                        ui.nickname,
                        ui.email,
                        ui.birth_date
                    FROM posts as p
                    JOIN users_info as ui ON p.id_author = ui.id
                    WHERE p.id = :id

                    UNION ALL 

                    SELECT 
                        p.id, 
                        p.nm_title, 
                        p.dt_created, 
                        ui.nickname, 
                        ui.email,
                        ui.birth_date
                    FROM posts as p
                    JOIN users_info as ui ON p.id_author = ui.id
                    JOIN model as m ON p.parent_id = m.id
                    LIMIT 5
                )
                SELECT * FROM model;"""
            )
            return{
                "content":session.execute(text(query), params={"id":id}).all(),
                "status":"Founded",
                "message":"Post from %s created %s" % ("temp", "01-01-2000")
            }