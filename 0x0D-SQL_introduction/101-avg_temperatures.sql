-- temperatures

SOURCE /alx-higher_level_programming/0x0D-SQL_introduction/temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
