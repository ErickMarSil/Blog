CREATE TABLE posts (
    id SERIAL NOT NULL PRIMARY KEY,
    nm_title VARCHAR(25) NOT NULL,
    dt_created DATE NOT NULL,
    parent_id BIGINT,
    id_author BIGINT NOT NULL
);

CREATE OR REPLACE PROCEDURE psGetPostContent(id_code BIGINT) LANGUAGE plpgsql AS $$
    BEGIN
        WITH RECURSIVE model AS (
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
        SELECT * FROM model;
END; $$;