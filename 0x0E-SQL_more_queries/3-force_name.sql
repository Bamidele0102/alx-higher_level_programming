-- Creates the table force_name
-- Data in table: id INT, name VARCHAR(256) can’t be null
-- Database name will be passed as an argument of the mysql command
-- If table exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
