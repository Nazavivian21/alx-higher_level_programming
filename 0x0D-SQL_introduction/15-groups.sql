-- List all records of a table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
