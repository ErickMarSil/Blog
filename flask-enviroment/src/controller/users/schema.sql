CREATE TABLE hash (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    password_hash VARCHAR(64) NOT NULL, 
    salt VARCHAR(32) NOT NULL,
    user_id BIGSERIAL REFERENCES users_info (id)
);

CREATE TABLE users_info (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(16) NOT NULL,
    birth_date DATE NOT NULL
);