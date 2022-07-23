CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      -- 两次select保证return null
      SELECT (
          SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC LIMIT 1 OFFSET M
      )
  );
END



--Option 2
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        SELECT 
            CASE
                WHEN COUNT(*) < (@N) THEN NULL
                ELSE MIN(salary)
            END
        FROM (
            SELECT DISTINCT TOP (@N) salary
            FROM Employee
            ORDER BY salary DESC
        ) tmp
    );
END

/*
Note:
(1) 可以用在SELECT上面

CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;

(2) 变量名使用(@N)

*/