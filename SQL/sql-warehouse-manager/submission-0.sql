-- Write your query below
SELECT 
    w.name AS warehouse_name,
    SUM(w.units * (p.width * p.length * p.height)) AS volume
FROM products p
JOIN warehouse w USING(product_id)
GROUP BY w.name
