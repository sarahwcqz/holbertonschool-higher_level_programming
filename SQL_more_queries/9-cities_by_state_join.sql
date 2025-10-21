-- lists all cities of DB
-- use outer join
SELECT cities.id, cities.name, states.name
FROM cities LEFT OUTER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
