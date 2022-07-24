-- Option 1
select person1, person2, count(*) as call_count, sum(duration) as total_duration from (
select from_id as person1, to_id as person2, duration
from Calls
union all
select to_id as person1, from_id as person2, duration
from Calls ) u
where person1 < person2
group by person1, person2