Problem Statement: Implement a solution for: Calculate Factorial. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 90: Calculate Factorial
// Optimize for performance

function factorial(n) {
    if (n === 0) return 1;
    return n * factorial(n - 1);
}
console.log(factorial(5));
```
