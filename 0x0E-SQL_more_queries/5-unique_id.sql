-- Creates the table unique_id
-- Description of table data: id INT with the default value 1, must be unique & name VARCHAR(256)
-- Should not fail if exists

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
