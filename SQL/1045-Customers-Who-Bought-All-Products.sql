# Write your MySQL query statement below
with tmp as (
    select *
    from Customer
    where product_key in (select * from Product)
)

select customer_id
from tmp
group by customer_id
having count(distinct product_key) = (select count(product_key) from Product)