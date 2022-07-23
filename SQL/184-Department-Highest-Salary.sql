-- Option 1
select d.name as Department, e.name as Employee, m.max_salary as Salary from
(select departmentId, max(salary) as max_salary
from Employee
group by departmentId) m
left join Employee e
on e.salary = m.max_salary and e.departmentId = m.departmentId
left join Department d
on d.id = e.departmentId

-- Option 2

select d.name as Department, m.name as Employee, m.salary as Salary
from Department d
left join
(SELECT departmentId, salary, name, RANK() OVER (PARTITION BY departmentID ORDER BY salary DESC) rnk
FROM Employee) m
on d.id = m.departmentId
where rnk = 1

/*
+----+-------+--------+--------------+
| id | name  | salary | departmentId | 
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            | 
| 2  | Jim   | 90000  | 1            | 
| 3  | Henry | 80000  | 2            | 
| 4  | Sam   | 60000  | 2            | 
| 5  | Max   | 90000  | 1            | 
+----+-------+--------+--------------+

by rank

+----+-------+--------+--------------+
| id | name  | salary | departmentId | rank
+----+-------+--------+--------------+
| 2  | Jim   | 90000  | 1            | 1
| 5  | Max   | 90000  | 1            | 1
| 1  | Joe   | 70000  | 1            | 2
| 3  | Henry | 80000  | 2            | 1
| 4  | Sam   | 60000  | 2            | 2
+----+-------+--------+--------------+

*/