
with tmp1 as (
    select s.amount,
           left(s.pay_date, 7) as pay_month,
           e.department_id
    from Salary s
    left join Employee e
    on s.employee_id = e.employee_id
    )

select distinct pay_month,
       department_id,
       case
           when (avg(amount) over(partition by pay_month)) > (avg(amount) over(partition by pay_month, department_id)) then 'lower'
           when (avg(amount) over(partition by pay_month)) < (avg(amount) over(partition by pay_month, department_id)) then 'higher'
           else 'same'
       end as comparison
from tmp1
