Problem Statement: Implement a solution for: Sum of Array. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 126: Sum of Array
// Optimize for performance

function sumArray(arr) {
    return arr.reduce((a, b) => a + b, 0);
}
console.log(sumArray([1, 2, 3]));
```
