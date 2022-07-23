select followee as follower, count(*) as num
from Follow
where followee in (select distinct follower from Follow)
group by followee