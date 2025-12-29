Problem Statement: Write an SQL query to retrieve the name, age, and city of all individuals from the "people" table who are older than 30 years old and live in New York City. Return the result sorted by descending ages. If multiple people share their birthdate (i.e., have same age), sort them alphabetically by last names first then first names as tie-breaker, if necessary.

Solution Code:

```sql
SELECT name, age, city 
FROM `people`
WHERE age > 30 AND city = 'New York City'
ORDER BY age DESC, (last_name || ', ' || first_name) ASC;
```
Explanation of Solution code logic: The query begins with selecting the desired columns from "people" table. It then applies a filter to include only rows where age is greater than 30 and city is New York City using `WHERE` clause conditions, followed by sorting on 'age' in descending order first (to display older individuals at top) and for people who have same ages alphabetically based upon their full names `(last_name || ', '|| first_name)` as a tie-breaker. 
The output will consist of the name(s), age, city information from all such eligible records in New York City sorted by descending order of age and then ascending (alphabetical) based on full names if same ages exist.
