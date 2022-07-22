/*
case
when condition1 then result1
when condition2 then result2
end
*/
update Salary
set sex =
case
when sex = 'f' then 'm'
when sex = 'm' then 'f'
end