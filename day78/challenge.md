Problem Statement: Implement a solution for: Check Palindrome. Provide an optimal solution using JavaScript.

Solution Code:
```javascript
// Day 78: Check Palindrome
// Optimize for performance

function isPalindrome(s) {
    return s === s.split('').reverse().join('');
}
console.log(isPalindrome('racecar'));
```
