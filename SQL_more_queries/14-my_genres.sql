-- Use the database for list all genre of Dexter
SELECT DISTINCT COUNT(tv_genres.name) as name
FROM tv_shows_genre LEFT JOIN tv_genres_id = tv_shows_genre.genre_id WHERE tv_shows.title is Dexter
ORDER BY name ASC;