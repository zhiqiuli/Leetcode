with tmp1 as (
    select buyer_id, count(*) as orders_in_2019
    from Orders
    where order_date between '2019-01-01' and '2019-12-31'
    group by buyer_id)

select u.user_id as buyer_id, u.join_date, isnull(t.orders_in_2019, 0) as orders_in_2019
from Users u
left join tmp1 t
on u.user_id = t.buyer_id