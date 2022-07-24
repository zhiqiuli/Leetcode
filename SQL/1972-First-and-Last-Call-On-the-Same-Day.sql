WITH CTE AS (
    SELECT caller_id AS user_id, call_time, recipient_id FROM Calls
    UNION 
    SELECT recipient_id AS user_id, call_time, caller_id AS recipient_id FROM Calls
    ),
    
CTE1 AS ( 
    SELECT 
    user_id,
    recipient_id,
    cast(call_time as date) AS DAY,
    DENSE_RANK() OVER(PARTITION BY user_id, cast(call_time as date) ORDER BY call_time ASC ) AS RN,
    DENSE_RANK() OVER(PARTITION BY user_id, cast(call_time as date) ORDER BY call_time DESC) AS RK -- the last call of user_id at a date
    FROM CTE
    )

/*
CTE1

{"headers":
["user_id", "recipient_id", "DAY", "RN", "RK"],
"values": [
[1 , 5 , "2021-08-11", 1, 1], 
[3 , 11, "2021-08-17", 2, 1], 
[3 , 8 , "2021-08-17", 1, 2], 
[4 , 8 , "2021-08-24", 2, 1], 
[4 , 8 , "2021-08-24", 1, 2], 
[5 , 1 , "2021-08-11", 1, 1], 
[8 , 11, "2021-08-17", 2, 1], 
[8 , 3 , "2021-08-17", 1, 2], 
[8 , 4 , "2021-08-24", 2, 1], 
[8 , 4 , "2021-08-24", 1, 2], 
[11, 8 , "2021-08-17", 2, 1], 
[11, 3 , "2021-08-17", 1, 2]]}
*/

SELECT DISTINCT user_id
FROM CTE1
WHERE RN = 1 OR RK = 1 -- 选出每天的第一个和最后一个
GROUP BY user_id, DAY
HAVING COUNT(DISTINCT recipient_id) = 1 -- 确保第一个和最后一个的recipient_id只有一个，说明只和一个人通电话
