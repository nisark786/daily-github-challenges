Problem Statement: Implement a solution for: Check Palindrome. Provide an optimal solution using SQL.

Solution Code:
```sql
-- Day 62: Check Palindrome
-- Query optimization

SELECT * FROM words WHERE word = REVERSE(word);
```
