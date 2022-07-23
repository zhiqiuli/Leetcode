-- re-arrange the table order by new_id
select rank() over (order by new_id) as id, student
from (
    -- all even number minus one
    select id - 1 as new_id, student
    from Seat
    where id % 2 = 0
    
    union all
    
    -- all odd number plus one
    select id + 1 as new_id, student
    from Seat
    where id % 2 <> 0) m