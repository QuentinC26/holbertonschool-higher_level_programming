-- list all cities contained in the database
SELECT id, name, state_id as name FROM cities;
INNER JOIN states ON cities.state_id = states.name