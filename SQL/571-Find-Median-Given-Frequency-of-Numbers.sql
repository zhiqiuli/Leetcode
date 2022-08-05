'''
num, freq, rk1, rk2, abs(rk1 - rk2)
0  , 7   , 7  , 12 , 5 <- abs(rk1 - rk2) <= frequency
1  , 1   , 8  , 5  , 3
2  , 3   , 11 , 4  , 7
3  , 1   , 12 , 1  , 11
'''
with tmp1 as (
            SELECT num, frequency,
            SUM(Frequency) OVER (ORDER BY num ASC) rk1,
            SUM(Frequency) OVER (ORDER BY num DESC) rk2
            FROM Numbers)

select avg(num * 1.0) as median
from tmp1
where abs(rk1 - rk2) <= frequency