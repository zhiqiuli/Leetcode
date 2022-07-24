/*
(1) ROUND(3.1415, 2) = 3.14

(2) the division in the SQL for integers cannot automatically do type transform
*/

--Option 1

select Day, round(sum(cancel) / count(*), 2) as 'Cancellation Rate'
from (
    select request_at as Day, (case
                               when status = 'cancelled_by_driver' then 1.0
                               when status = 'cancelled_by_client' then 1.0
                               else 0.0 end) as cancel
    from Trips
    where client_id in (select distinct users_id from Users where banned = 'No') and driver_id in (select distinct users_id from Users where banned = 'No')
    ) m
where Day between '2013-10-01' and '2013-10-03'
group by Day
order by Day

--Option 2
select request_at as Day, round(sum(case
                                    when status = 'cancelled_by_driver' then 1.0
                                    when status = 'cancelled_by_client' then 1.0
                                    else 0.0 end) / count(*), 2) as 'Cancellation Rate'
from Trips
where client_id in (select distinct users_id from Users where banned = 'No') and driver_id in (select distinct users_id from Users where banned = 'No')
and request_at between '2013-10-01' and '2013-10-03'
group by request_at
order by request_at
