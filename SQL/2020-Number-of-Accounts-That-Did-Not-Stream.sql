select count(distinct account_id) as accounts_count
from Subscriptions
where 2021 between year(start_date) and year(end_date) and account_id not in (
    select distinct account_id
    from Streams
    where year(stream_date) = 2021)