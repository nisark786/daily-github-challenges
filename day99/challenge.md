Problem Statement: Implement a solution for: Check Anagram. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 99: Check Anagram
// Optimize for performance

function isAnagram(s1, s2) {
    return s1.split('').sort().join('') === s2.split('').sort().join('');
}
console.log(isAnagram('listen', 'silent'));
```
