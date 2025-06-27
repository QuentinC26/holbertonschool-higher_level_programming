-- list all genres contained in database and dsiplays the number of shows linked to each
SELECT DISTINCT name as genre, COUNT(tv_show_genres.show_id) as number_of_shows 
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;