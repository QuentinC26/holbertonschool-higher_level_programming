-- Use the database for list all genre of Dexter
SELECT DISTINCT COUNT(tv_genres.name) as name
FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_genres.name ASC;