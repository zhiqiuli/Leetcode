temp0 AS (
    SELECT  id,
            login_date,
            dense_rank() OVER (PARTITION BY id ORDER BY login_date) as row_num
    FROM Logins),

temp1 as (
    select id,
           login_date,
           row_num,
           DATEADD(day, -row_num, login_date) as Groupings
    from temp0),
    
/*
select *
from temp1

{"headers":
 ["id", "login_date", "row_num", "Groupings"],
"values":
[[1, "2020-05-30", 1, "2020-05-29"],
 [1, "2020-06-07", 2, "2020-06-05"],
 [7, "2020-05-30", 1, "2020-05-29"],
 [7, "2020-05-31", 2, "2020-05-29"],
 [7, "2020-06-01", 3, "2020-05-29"],
 [7, "2020-06-02", 4, "2020-05-29"],
 [7, "2020-06-02", 4, "2020-05-29"],
 [7, "2020-06-03", 5, "2020-05-29"],
 [7, "2020-06-10", 6, "2020-06-04"]]}
 
 this gives a constant value in Groupings for consecutive rows.
 You can then group by this colum to get the summary you want.
*/

answer_table as (
         SELECT id,
                Groupings,
                MIN(login_date) as startDate,
                MAX(login_date) as EndDate,
                count(*) as number_of_5_consecutive_days,
                datediff(day, MIN(login_date), MAX(login_date)) as duration
 FROM temp1
 GROUP BY id, Groupings
 HAVING datediff(day, MIN(login_date), MAX(login_date)) >= 4)

select distinct a.id, aa.name
from answer_table a
left join Accounts aa
on a.id = aa.id




-- Option 2

/*SELECT DISTINCT a.id
    , (SELECT name FROM accounts WHERE id=a.id) AS name
FROM logins a, logins b
WHERE a.id = b.id AND DATEDIFF(day, a.login_date, b.login_date) BETWEEN 1 AND 4
GROUP BY a.id, a.login_date
HAVING COUNT(DISTINCT b.login_date) = 4

Example 1

a login_date 1 2 3 4 5
b login_date 1 2 3 4 5

a b b b b
1 2 3 4 5
2 3 4 5
3 4 5
4 5

b has four 5's so we have the last condition HAVING COUNT(DISTINCT b.login_date) = 4

Example 2

a login_date 1 2 3 5 6
b login_date 1 2 3 5 6

a b b b
1 2 3 5
2 3 5 6
3 5 6
5 6

b doesn't have 5's so the last condition WON'T SATISFY

*/

SELECT DISTINCT a.id
    , (SELECT name FROM accounts WHERE id=a.id) AS name
FROM logins a, logins b
WHERE a.id = b.id AND DATEDIFF(day, a.login_date, b.login_date) BETWEEN 1 AND 4
GROUP BY a.id, a.login_date
HAVING COUNT(DISTINCT b.login_date) = 4