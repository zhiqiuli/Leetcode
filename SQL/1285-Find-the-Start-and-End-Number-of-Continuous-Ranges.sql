with tmp1 as (
    select log_id, row_number() over (order by log_id) - log_id as rk_group
    from Logs)

select min(log_id) as start_id, max(log_id) as end_id
from tmp1
group by rk_group
order by start_id, end_id