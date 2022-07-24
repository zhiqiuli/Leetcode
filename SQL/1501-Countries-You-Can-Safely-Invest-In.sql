with tmp1 as (
         select id, c.name
         from Person p
         left join Country c
         on substring(p.phone_number,1,3) = c.country_code),
     tmp2 as (
         select caller_id as id, duration
         from Calls
         union all
         select callee_id as id, duration
         from Calls)

select tmp1.name as country
from tmp1
left join tmp2
on tmp1.id = tmp2.id
group by tmp1.name
having avg(tmp2.duration) > (select avg(duration) from Calls)