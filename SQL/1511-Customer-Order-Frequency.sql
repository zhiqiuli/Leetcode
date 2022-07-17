# Write your MySQL query statement below
select customer_id, name
from (select c.customer_id, c.name,
SUM(CASE WHEN (o.order_date between '2020-06-01' and '2020-06-30') THEN p.price*o.quantity ELSE 0 END) AS t1,
SUM(CASE WHEN (o.order_date between '2020-07-01' and '2020-07-31') THEN p.price*o.quantity ELSE 0 END) AS t2
from Orders o
join Product p
on p.product_id = o.product_id
join Customers c
on o.customer_id = c.customer_id
group by 1) tmp
where tmp.t1 >= 100 and tmp.t2 >= 100
