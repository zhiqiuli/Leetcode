/*
此处使用sum的目的是为了再用group by，group by sum之后，null sum即可消失。

假设不使用sum

select id, 
(case month when 'Jan' then revenue else Null end) as Jan_Revenue
from Department

{"headers": ["id", "Jan_Revenue"], "values": [[1, 8000], [2, 9000], [3, null], [1, null], [1, null]]}
*/

select id, 
sum(case month when 'Jan' then revenue else Null end) as Jan_Revenue, 
sum(case month when 'Feb' then revenue else Null end) as Feb_Revenue,
sum(case month when 'Mar' then revenue else Null end) as Mar_Revenue,
sum(case month when 'Apr' then revenue else Null end) as Apr_Revenue,
sum(case month when 'May' then revenue else Null end) as May_Revenue,
sum(case month when 'Jun' then revenue else Null end) as Jun_Revenue,
sum(case month when 'Jul' then revenue else Null end) as Jul_Revenue,
sum(case month when 'Aug' then revenue else Null end) as Aug_Revenue,
sum(case month when 'Sep' then revenue else Null end) as Sep_Revenue,
sum(case month when 'Oct' then revenue else Null end) as Oct_Revenue,
sum(case month when 'Nov' then revenue else Null end) as Nov_Revenue,
sum(case month when 'Dec' then revenue else Null end) as Dec_Revenue
from Department
group by id