/*
HAVING Clause

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
*/

select email as Email
from Person
group by email
having count(email) > 1