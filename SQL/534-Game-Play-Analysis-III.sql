/*
Option 1

Use the cumulative sum for over the partition
*/

select player_id, 
       event_date, 
       sum(games_played) over (partition by player_id order by player_id, event_date) as games_played_so_far
from Activity

-- Option 2
select b.player_id, b.event_date, sum(row.games_played) as games_played_so_far
from Activity row, Activity b
where row.event_date <= b.event_date and row.player_id = b.player_id
group by b.player_id, b.event_date
order by b.player_id, b.event_date