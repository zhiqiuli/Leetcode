Notes:

1. subquery must use an alias

select *
from (select * from subquery_table) u

2. distinct a, b, c -> 选出unique的a, b, c;

3. count(unique a) -> count()里面也可以使用unique

4. ROUND(3.1415, 2) = 3.14

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

8. cumulative sum
	SELECT
	SUM(salary) over(order by salary) as rn
	FROM Candidates

9. ISNULL(NULL, 0) return 0 if var is NULL

10. LAG(arrival_time, 1, 0) OVER (ORDER BY arrival_time) t_before, --LAG('return value', 'offset', 'default value')

11. DATEADD(interval, number, date)

12. cumsum...

see 534

13. island problem...

see 1811