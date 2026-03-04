Problem Statement: Implement a solution for: Find Prime Numbers. Provide an optimal solution using SQL.

Solution Code:
```sql
-- Day 71: Find Prime Numbers
-- Query optimization

SELECT n FROM numbers n1 WHERE NOT EXISTS (SELECT 1 FROM numbers n2 WHERE n2.n > 1 AND n2.n < n1.n AND n1.n % n2.n = 0);
```
