WITH TMP1 AS (
    SELECT DISTINCT sell_date, product
    FROM Activities)

SELECT 
    sell_date,
    COUNT(product) AS num_sold,
    STRING_AGG(product, ',') WITHIN GROUP (ORDER BY PRODUCT) AS products
FROM TMP1
GROUP BY sell_date