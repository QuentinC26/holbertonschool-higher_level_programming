-- Use the database for list all genre of Dexter
SELECT name
FROM tv_shows LEFT JOIN tv_genres ON tv_shows.id = tv_genres.id WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;