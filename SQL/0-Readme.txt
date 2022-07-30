Notes:

1. subquery must use an alias

	select *
	from (select * from subquery_table) u

2. distinct a, b, c -> 选出unique的a, b, c;

3. count(unique a) -> count()里面也可以使用unique

4. Some handful functions for dates, numbers, and strings,

	  YEAR('2021-1-4') = 2021
     DATEADD(day, 1, '2020-9-11') = '2021-9-12' # DATEADD(interval, numbers, date)
     DATEDIFF(day, '2020-9-11', '2020-9-15') = 4 # DATEDIFF(interval, date1, date2)

     ROUND(3.1415, 2) = 3.14
     SELECT CAST(col as float) ... = 1.0 or SELECT 1.0 * col as col
     
     CONCAT('x', '+', 'y')  = 'x+y'
     SUBSTRING('xyz', 1, 2) = 'xy'
     STRING_AGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
     		=> 'a','b','c' => 'a,b,b'

     ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...) as RN => row number   a, b, b, c, d -> 1, 2, 3, 4, 5
     RANK()       OVER (PARTITION BY ... ORDER BY ...) as RK =>       rank   a, b, b, c, d -> 1, 2, 2, 4, 5
     DENSE_RANK() OVER (PARTITION BY ... ORDER BY ...) as RK => dense rank   a, b, b, c, d -> 1, 2, 2, 3, 4
     COUNT(*)     OVER (PARTITION BY ...)                    => 

     Moving average ...
     SUM(SUM(amount)) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS 'Amount'


5. the division in the SQL for integers cannot automatically do type transform

6.  case
		when ... then ...
		when ... then ...
		else ..
    end

7. WITH table_name as (SELECT...) define a temporary table
   for multiple tables, use one WITH

with temp1 as (select * from table1),
     temp2 as (select * from table2)

8. cumulative sum for a column (see 534)
	
	Option 1

	SELECT SUM(salary) over(order by salary) as rn
	FROM Candidates

	Option 2

	INNER JOIN & GROUP BY

9. ISNULL(NULL, 0) return 0 if var is NULL

10. LAG(arrival_time, 1, 0) OVER (ORDER BY arrival_time) t_before, --LAG('return value', 'offset', 'default value')

11. island problem...

see 1811

12. REVIEW 1484 & 1321 (2022/7/27)

13. -- only shows last 6 rows
	 OFFSET 6 ROWS
