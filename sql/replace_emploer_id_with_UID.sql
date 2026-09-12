-- Write your PostgreSQL query statement below
SELECT er.unique_id, el.name
FROM  Employees el
LEFT JOIN EmployeeUNI er
-- USING (id);
ON el.id = er.id
ORDER BY name ASC;