-- Use the database for list all genre of Dexter
SELECT COUNT(tv_show_genres.show_id) AS name
FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.show_id = tv_genres.id WHERE tv_show_genres.show_id = 8
GROUP BY (tv_show_genres.genre_id)
ORDER BY tv_genres.name ASC;