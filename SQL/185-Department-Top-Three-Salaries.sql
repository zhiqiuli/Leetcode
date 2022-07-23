select d.name as Department, m.name as Employee, m.salary as Salary
from (select id, name, salary, departmentId, dense_rank() over (partition by departmentId order by salary desc) rnk
from Employee) m
left join Department d
on m.departmentId = d.id
where m.rnk <= 3
order by m.id asc, m.salary desc