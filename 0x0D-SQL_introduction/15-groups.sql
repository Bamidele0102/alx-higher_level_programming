-- Lists the number of records with the samscore in the table second_table in my MySQL server.
-- Records are ordered by descending count.

SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC;
