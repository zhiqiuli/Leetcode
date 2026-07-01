with tmp as (
    select u.product_id, u.units, p.price
    from UnitsSold u
    left join Prices p
    on u.product_id = p.product_id
        and u.purchase_date >= p.start_date
        and u.purchase_date <= p.end_date
),
tmp2 as (
    select product_id, round(sum(units * price) / sum(units), 2) as average_price
    from tmp
    group by product_id
    order by product_id
)
-- remember the function ifnull
select p.product_id, ifnull(t.average_price, 0) as average_price
from (select distinct product_id from Prices) p
left join tmp2 t
on p.product_id = t.product_id