-- Write your query below
SELECT name 
FROM customers c
LEFT JOIN orders o 
    ON c.id = o.customer_id
WHERE c.id NOT IN (SELECT customer_id FROM orders )

