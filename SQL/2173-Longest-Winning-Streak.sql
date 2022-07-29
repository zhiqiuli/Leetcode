with tmp1 as (
    select player_id, result, row_number() over (partition by player_id order by match_day) as RN
    from Matches),

tmp2 as (
    select player_id, result, RN, row_number() over (partition by player_id  order by RN) as RK
    from tmp1
    where result = 'Win'), -- create RK then filter with WHERE

tmp3 as (
    select player_id, result, RN, RN - RK as Group_RK
    from tmp2),

tmp4 as (
    select player_id, count(*) as longest_streak
    from tmp3
    group by Group_RK, player_id),
    
tmp5 as (
    select player_id, max(longest_streak) as longest_streak
    from tmp4
    group by player_id)

select distinct a.player_id, isnull(b.longest_streak, 0) as longest_streak
from Matches a
left join tmp5 b
on a.player_id = b.player_id
order by a.player_id