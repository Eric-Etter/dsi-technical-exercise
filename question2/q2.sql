/* 
# Technical Exercise, Question 2:
Write a SQL query that retrieves the names of all salespeople that have more than $1300 
in orders from the tables above. You can assume that each salesperson only has one ID.
*/

-- 
SELECT salesperson_id, amount
FROM orders
GROUP BY salesperson_id;