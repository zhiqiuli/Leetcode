select (case 
        when (select count(score) from NewYork where score >= 90) > (select count(score) from California where score >= 90) then 'New York University'
        when (select count(score) from NewYork where score >= 90) < (select count(score) from California where score >= 90) then 'California University'
        else 'No Winner'
        end) as winner