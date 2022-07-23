select t.team_name, count(*) as matches_played, sum(m.point) as points, sum(goal) as goal_for, sum(ngoal) as goal_against, sum(goal) - sum(ngoal) as goal_diff
from (
    select home_team_id as team, home_team_goals as goal, away_team_goals as ngoal,
        case
            when home_team_goals > away_team_goals then 3
            when home_team_goals = away_team_goals then 1
            else 0
        end as point
    from Matches

    union all --'union all' keeps the duplicated records; 'union' will discard the duplicated records

    select away_team_id as team, away_team_goals as goal, home_team_goals as ngoal,
        case
            when away_team_goals > home_team_goals then 3
            when away_team_goals = home_team_goals then 1
            else 0
        end as point
    from Matches
) m
left join Teams t
on m.team = t.team_id
group by t.team_name
order by points desc, goal_diff desc, t.team_name