-- Use the database for list all genre of Dexter
SELECT DISTINCT COUNT(tv_genres.name) as name
FROM tv_shows_genres LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id;
WHERE tv_shows.title IS Dexter
ORDER BY name ASC;