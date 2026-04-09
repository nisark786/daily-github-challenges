Problem Statement: Implement a solution for: Calculate Factorial. Provide an optimal solution using SQL.

Solution Code:
```sql
-- Day 107: Calculate Factorial
-- Query optimization

WITH RECURSIVE fact(n, f) AS (
  SELECT 1, 1
  UNION ALL
  SELECT n+1, f*(n+1) FROM fact WHERE n < 5
)
SELECT f FROM fact WHERE n = 5;
```
