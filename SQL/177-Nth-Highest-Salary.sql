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