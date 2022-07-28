with sum_amounts as (
    select visited_on, sum(amount) as amount
    from Customer
    group by visited_on),
/*
{"headers": ["visited_on", "amount"], "values": [
["2019-01-01", 100], 
["2019-01-02", 110], 
["2019-01-03", 120], 
["2019-01-04", 130], 
["2019-01-05", 110], 
["2019-01-06", 140], 
["2019-01-07", 150], 
["2019-01-08", 80], 
["2019-01-09", 110], 
["2019-01-10", 280]]}
*/

amount_sum AS (
    SELECT visited_on,
    SUM(amount)       OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    AVG(amount * 1.0) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
    FROM sum_amounts
    GROUP BY visited_on, amount)

SELECT visited_on, round(amount, 2) as amount, round(average_amount, 2) as average_amount
FROM amount_sum
WHERE visited_on NOT IN (SELECT TOP 6 visited_on FROM customer GROUP BY visited_on)
ORDER BY visited_on ASC;