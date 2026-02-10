Problem Statement: Implement a solution for: Check Anagram. Provide an optimal solution using Python.

Solution Code:
```python
# Day 49: Check Anagram
# Time complexity varies based on implementation

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram('listen', 'silent'))
```
