Problem Statement: Implement a solution for: Count Vowels. Provide an optimal solution using Python.

Solution Code:
```python
# Day 121: Count Vowels
# Time complexity varies based on implementation

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels('hello'))
```
