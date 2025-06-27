-- Use the database for list all genre of Dexter
SELECT name
FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_show_genres.genre_id = 8
ORDER BY tv_genres.name ASC;