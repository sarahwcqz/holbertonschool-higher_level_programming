-- creates a table 'unique_id'
-- to learn how to set a unique attribute
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
