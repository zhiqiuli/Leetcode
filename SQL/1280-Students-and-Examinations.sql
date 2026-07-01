with tmp1 as (
    select *
    from Students
    # cross join is used to BROADCAST the rows into another table
    cross join Subjects
),

tmp2 as (
    select student_id, subject_name, count(*) as attended_exams
    from Examinations
    group by student_id, subject_name
)

# COALESCE replaces the left join null with 0
select tmp1.student_id, tmp1.student_name, tmp1.subject_name, COALESCE(tmp2.attended_exams, 0) as attended_exams
from tmp1
left join tmp2
on tmp1.student_id = tmp2.student_id and tmp1.subject_name = tmp2.subject_name
order by tmp1.student_id, tmp1.subject_name
