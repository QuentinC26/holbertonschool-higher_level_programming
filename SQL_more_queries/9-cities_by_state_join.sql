-- list all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities, states;
JOIN states ON cities.id = states.id;
ORDER BY cities.id ASC