-- lists the number of records with the same score
SELECT DISTINCT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC 