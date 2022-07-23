SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'RANK'
FROM Scores

/*
DENSE_RANK() and RANK()

Syntax:

DENSE_RANK() OVER (
    [PARTITION BY partition_expression, ... ]
    ORDER BY sort_expression [ASC | DESC], ...
)

Example:

SELECT
	v,
	DENSE_RANK() OVER (
		ORDER BY v
	) my_dense_rank,
	RANK() OVER (
		ORDER BY v
	) my_rank
FROM
	sales.dense_rank_demo;

v my_dense_rank my_rank
A 1             1
B 2             2
B 2             2
C 3             4
C 3             4
D 4             6
E 5             7

More complicated with PARTITION

SELECT * FROM (
	SELECT
		product_id,
		product_name,
		category_id,
		list_price,
		DENSE_RANK () OVER ( 
			PARTITION BY category_id
			ORDER BY list_price DESC
		) price_rank 
	FROM
		production.products
) t
WHERE price_rank < 3;
*/