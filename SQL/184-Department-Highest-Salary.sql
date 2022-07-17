# Write your MySQL query statement below
select d.name as Department, e.name Employee, salary as Salary
from Department d, Employee e
where d.id = e.departmentId -- 相当于是join table了，这种情况一定会match的话，可以同时select两个table然后
and
(departmentId, salary) in (
select departmentId, max(salary)
from Employee
group by departmentId
)