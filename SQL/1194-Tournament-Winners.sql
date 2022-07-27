with tmp1 as (
    select match_id, first_player as player_id, first_score as score
    from Matches
    union all
    select match_id, second_player as player_id, second_score as score
    from Matches),
    
tmp2 as (
    select p.group_id, p.player_id, sum(t.score) as total_score
    from tmp1 t
    left join Players p
    on t.player_id = p.player_id
    group by p.group_id, p.player_id),

tmp3 as (select group_id,
                player_id,
                total_score,
                -- rank()这个语句一定要记住！当有重复的elements时，dense_rank()生成1,1,2和rank()生成1,1,3
                rank() over (partition by group_id order by total_score desc, player_id) as RK
         from tmp2)

select group_id as GROUP_ID, player_id as PLAYER_ID
from tmp3
where RK = 1    