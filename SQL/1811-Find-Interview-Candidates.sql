with t0 as  (
    select gold_medal as user_id, contest_id 
    from Contests
    union all
    select silver_medal as user_id, contest_id 
    from Contests
    union all
    select bronze_medal as user_id, contest_id 
    from Contests),
/*
{"headers": ["user_id", "contest_id"], "values": [
[1, 190], 
[2, 191], 
[5, 192], 
[1, 193], 
[4, 194], 
[4, 195], 
[1, 196], 
[5, 190], 
[3, 191], 
[2, 192], 
...
*/

t1 as (
    select user_id, contest_id, dense_rank() over(partition by user_id order by contest_id) as rn 
    from t0),

/*
select user_id, contest_id, contest_id - rn
from t1

{"headers": ["user_id", "contest_id", ""],
"values": [
[1, 190, 189], 
[1, 193, 191], 
[1, 195, 192], 
[1, 196, 192], 
[2, 190, 189], 
[2, 191, 189], 
[2, 192, 189], 
[2, 194, 190], 
[2, 195, 190], 
[2, 196, 190], 
[3, 191, 190], 
[3, 192, 190], 
[3, 193, 190], 
[4, 194, 193], 
[4, 195, 193], 
...
*/

t2 as (
    select user_id -- consecutive medal winners
    from t1 
    group by user_id, contest_id - rn -- !!!KEY!!! GROUP BY USER then DATE-RN 
    having count(*) >= 3 -- replace 3 with any number to solve the N problem
    union all
    select gold_medal as user_id  -- gold medal winners
    from contests 
    group by gold_medal 
    having count(*) >= 3
)

select distinct name, mail
from Users u
right join t2 t
on u.user_id = t.user_id
