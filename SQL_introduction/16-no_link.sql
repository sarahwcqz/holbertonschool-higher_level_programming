-- lists all records of a table
-- doesn't show rows where name is null
-- displays score by descending and name
SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;
