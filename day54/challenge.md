Problem Statement: Implement a solution for: Find Prime Numbers. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 54: Find Prime Numbers
// Optimize for performance

function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}
console.log(isPrime(7));
```
