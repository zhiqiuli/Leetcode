/*
Notes:

(1) WITH table_name as (SELECT...) define a temporary table
(2) cumulative sum
	SELECT
	SUM(salary) over(order by salary) as rn
	FROM Candidates
(3) ISNULL(NULL, 0) return 0 if var is NULL
*/

WITH CTE AS (SELECT employee_id, experience, SUM(salary) OVER(PARTITION BY experience ORDER BY salary) AS RN FROM Candidates)

SELECT 'Senior' AS experience, COUNT(employee_id) AS accepted_candidates
FROM CTE
WHERE experience = 'Senior' AND RN <= 70000

UNION

SELECT 'Junior' AS experience, COUNT(employee_id) AS accepted_candidates
FROM CTE
WHERE experience = 'Junior' AND RN <= (SELECT 70000 - ISNULL(MAX(RN), 0) FROM CTE WHERE experience = 'Senior' AND RN <= 70000)