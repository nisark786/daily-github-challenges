Problem Statement: Implement a solution for: Count Vowels. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 39: Count Vowels
// Optimize for performance

function countVowels(s) {
    const match = s.match(/[aeiou]/gi);
    return match ? match.length : 0;
}
console.log(countVowels('hello'));
```
