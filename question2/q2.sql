/* DSI Technical Exercise - Question 2
Write a SQL query that retrieves the names of all salespeople that have more than $1300 in orders from the tables above. 
You can assume that each salesperson only has one ID. */

SELECT salesperson.name, orders.amount
FROM orders 
JOIN salesperson
ON salesperson.id = orders.salesperson_id
GROUP BY salesperson.id;
