--MS SQL Server

--The GROUP BY statement is often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()) to group the result-set by one or more columns.


select top 1 customer_number
from Orders
group by customer_number
order by count(order_number) desc