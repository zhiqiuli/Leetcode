-- Option 1

# Get each passenger's boarding time
WITH t AS
(
    SELECT passenger_id, MIN(b.arrival_time) AS arrival_time
    FROM Passengers p
    INNER JOIN Buses b
    ON p.arrival_time <= b.arrival_time
    GROUP BY passenger_id
)

# Boarding time and bus id have 1 to 1 correspondence
SELECT bus_id, COUNT(t.arrival_time) AS passengers_cnt
FROM Buses b
LEFT JOIN t
ON b.arrival_time = t.arrival_time
GROUP BY bus_id
ORDER BY bus_id


-- Option 2

WITH t1 AS 
      (SELECT bus_id, IFNULL(LAG(arrival_time) OVER(ORDER BY arrival_time), 0) t_before, arrival_time
       FROM Buses)
       -- LAG(arrival_time, 1, 0) OVER (ORDER BY arrival_time) t_before, --LAG('return value', 'offset', 'default value')

SELECT t1.bus_id, COUNT(p.passenger_id) passengers_cnt
FROM t1
LEFT JOIN Passengers p ON p.arrival_time > t1.t_before AND p.arrival_time <= t1.arrival_time
GROUP BY 1
ORDER BY 1 ASC