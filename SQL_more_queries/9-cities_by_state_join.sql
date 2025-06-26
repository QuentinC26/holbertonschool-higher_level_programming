-- list all cities contained in the database
SELECT id, name, state_id as name FROM cities ORDER BY id;
INNER JOIN states ON cities.state_id = states.name