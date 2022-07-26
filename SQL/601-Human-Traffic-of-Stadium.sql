with t1 as (
    select id,
           visit_date,
           people,
           dense_rank() over (order by id) rn
    from Stadium
    where people >= 100),
    
    t2 as (
    select id,
           visit_date,
           people,
           id - rn as rnn
    from t1)
    /*
    {"headers": ["id", "visit_date", "people", "rnn"], 
    "values": [
    [2, "2017-01-02", 109,  1], 
    [3, "2017-01-03", 150,  1], 
    [5, "2017-01-05", 145,  2], 
    [6, "2017-01-06", 1455, 2], 
    [7, "2017-01-07", 199,  2], 
    [8, "2017-01-09", 188,  2]]}
    */

select id, visit_date, people
from t2
where rnn in (
    select rnn
    from t2
    group by rnn
    having count(*) >= 3)
order by id