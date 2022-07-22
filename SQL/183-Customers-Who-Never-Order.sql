-- Option 1
/* Write your T-SQL query statement below */
select k.Customers from (
select a.name as Customers, b.id as Order_Id
from Customers a
left join Orders b
on a.id = b.customerId ) k -- You need to alias the subquery
where k.Order_Id is null


-- Option 2
/* Write your T-SQL query statement below */
select name as Customers
from Customers
where id not in (select distinct customerId from Orders)