-- Display the top 3 cities temperature
-- Display the highest temperature for 3 cities between July and August ordered by temperature

SELECT city, AVG(value) as 'avg_temp'
FROM temperatures
WHERE `month`=7 OR `month`=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
