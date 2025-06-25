-- create the table unique_id with unique default value for id 
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (ID)
);
