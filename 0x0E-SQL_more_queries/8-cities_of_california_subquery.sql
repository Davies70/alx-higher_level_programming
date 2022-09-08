-- cities of cali

SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
GROUP BY cities.id;
