with tmp1 as (
    select user_id, count(*) as confirmed
    from Confirmations
    where action = 'confirmed'
    group by user_id
),
tmp2 as (
    select user_id, count(*) as total
    from Confirmations
    group by user_id
),
tmp3 as (
    select tmp2.user_id, COALESCE(tmp1.confirmed / tmp2.total, 0) as confirmation_rate
    from tmp2
    left join tmp1
    on tmp2.user_id = tmp1.user_id
)
select s.user_id, ROUND(COALESCE(tmp3.confirmation_rate, 0), 2) as confirmation_rate
from Signups s
left join tmp3
on s.user_id = tmp3.user_id
order by s.time_stamp
