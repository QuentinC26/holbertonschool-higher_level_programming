-- list all cities contained in the database
SELECT id, name, states.name FROM cities ORDER BY id;
INNER JOIN states ON cities.state_id = states.state_id