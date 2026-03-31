-- Write your query below
SELECT DISTINCT email
FROM person
WHERE email NOT IN ( SELECT email
                    FROM person 
                    GROUP BY email
                    HAVING COUNT(email) = 1)
