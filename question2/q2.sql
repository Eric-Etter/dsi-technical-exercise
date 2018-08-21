/*
Write a SQL query that retrieves the names of all salespeople
that have more than $1300 in orders from the tables above. 
You can assume that each salesperson only has one ID.
*/ 

-- Create a common table expression (CTE) of the order sales by salesperson

WITH t1 as (
	SELECT salesperson_id, SUM(amount) AS total_order_sales
	FROM orders
	GROUP BY salesperson_id)

-- Join the above CTE to the salespersion table to gain access to the salespersons' name and add the where clause to filter on dollar value.

SELECT salesperson.name, total_order_sales
FROM t1
JOIN salesperson
ON t1.salesperson_id = salesperson.id
WHERE total_order_sales > 1300
ORDER BY total_order_sales DESC;