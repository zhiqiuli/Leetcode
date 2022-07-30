-- Option 1

with tmp1 as(
    select id, company, salary,
           row_number() over (partition by company order by company, salary) as rn,
           count(id)    over (partition by company) as cnt
    from Employee)

select id, company, salary
from tmp1
where rn between (cnt / 2.0) and (cnt / 2.0 + 1.0)

-- Option 2

with tmp1 as(
    select id, company, salary, row_number() over (partition by company order by company, salary) as rn
    from Employee),
tmp2 as (
    select company, (count(*) + 1) / 2 as position
    from Employee
    group by company
    having (count(*) % 2 <> 0)),
tmp3 as (
    select company, count(*) / 2 as position
    from Employee
    group by company
    having (count(*) % 2 = 0)
    union all
    select company, count(*) / 2 + 1 as position
    from Employee
    group by company
    having (count(*) % 2 = 0))

select e.id, e.company, e.salary
from tmp2 t
left join tmp1 e
on t.position = e.rn and t.company = e.company

union all

select e.id, e.company, e.salary
from tmp3 t
left join tmp1 e
on t.position = e.rn and t.company = e.company
