Problem Statement: Implement a solution for: Find Prime Numbers. Provide an optimal solution using Python.

Solution Code:
```python
# Day 70: Find Prime Numbers
# Time complexity varies based on implementation

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print(is_prime(7))
```
