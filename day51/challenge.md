Problem Statement: Implement a solution for: Remove Duplicates. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 51: Remove Duplicates
// Optimize for performance

function removeDup(arr) {
    return [...new Set(arr)];
}
console.log(removeDup([1, 1, 2]));
```
