Problem Statement: Implement a solution for: Count Vowels. Provide an optimal solution using SQL.

Solution Code:
```sql
-- Day 122: Count Vowels
-- Query optimization

SELECT LENGTH(name) - LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(name), 'a', ''), 'e', ''), 'i', ''), 'o', ''), 'u', '')) AS vowel_count FROM users;
```
