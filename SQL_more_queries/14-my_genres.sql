-- Use the database for list all genre of Dexter
SELECT name
FROM tv_genres
LEFT JOIN tv_shows ON tv_genres.id = tv_shows.id
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;