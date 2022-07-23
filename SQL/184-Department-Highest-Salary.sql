-- Option 1
select d.name as Department, e.name Employee, salary as Salary
from Department d, Employee e
where d.id = e.departmentId -- 相当于是join table了，这种情况一定会match的话，可以同时select两个table然后
and
(departmentId, salary) in (
select departmentId, max(salary)
from Employee
group by departmentId
)

-- Option 2
select d.name as Department, e.name as Employee, m.max_salary as Salary from
(select departmentId, max(salary) as max_salary
from Employee
group by departmentId) m
left join Employee e
on e.salary = m.max_salary and e.departmentId = m.departmentId
left join Department d
on d.id = e.departmentId