-- Option 1
select activity_date as day, count(user_id) as active_users
from (select distinct user_id, activity_date
      from Activity
      where activity_date between '2019-06-28' and '2019-07-27') u
group by activity_date


-- Option 2
SELECT activity_date as day, COUNT(distinct user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN '2019-6-28' AND '2019-7-27'
GROUP BY activity_date