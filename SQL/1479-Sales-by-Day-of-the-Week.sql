/* Write your T-SQL query statement below */
with tmp1 as (
    select i.item_category, datename(weekday, o.order_date) as dt, o.quantity
    from Orders o
    right join Items i
    on o.item_id = i.item_id)

select item_category as 'CATEGORY',
       sum(case when dt = 'Monday' then quantity else 0 end) as 'Monday',
       sum(case when dt = 'Tuesday' then quantity else 0 end) as 'Tuesday',
       sum(case when dt = 'Wednesday' then quantity else 0 end) as 'Wednesday',
       sum(case when dt = 'Thursday' then quantity else 0 end) as 'Thursday',
       sum(case when dt = 'Friday' then quantity else 0 end) as 'Friday',
       sum(case when dt = 'Saturday' then quantity else 0 end) as 'Saturday',
       sum(case when dt = 'Sunday' then quantity else 0 end) as 'Sunday'
from tmp1
group by item_category
