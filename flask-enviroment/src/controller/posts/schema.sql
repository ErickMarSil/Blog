CREATE TABLE posts (
    id SERIAL NOT NULL PRIMARY KEY,
    nm_title VARCHAR(25) NOT NULL,
    dt_created DATE NOT NULL,
    parent_id BIGINT,

    CONSTRAINT id_author FOREIGN KEY (id) REFERENCES users_info(id)
);