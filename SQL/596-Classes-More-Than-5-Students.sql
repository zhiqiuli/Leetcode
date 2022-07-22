/*
NOTE:group by 之后是没有where的，用的是having

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
*/

select class
from Courses
group by class
having count(student) >= 5