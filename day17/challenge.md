Problem Statement: Implement a solution for: Check Anagram. Provide an optimal solution using SQL.

Solution Code:
```sql
-- Day 17: Check Anagram
-- Query optimization

SELECT * FROM words WHERE word1 != word2 AND LENGTH(word1) = LENGTH(word2);
```
