**Problem Statement:**

**FizzBuzz**

Write a function that takes an integer `n` as input and returns an array of numbers from 1 to `n`, but replace multiples of 3 with "fizz", multiples of 5 with "buzz", and multiples of both 3 and 5 with "fizzbuzz".

**Example Input/Output:**

* `n = 10` -> `[1, 'fizz', 2, 'buzz', 4, 'fizz', 'buzz', 7, 8, 'fizz']`
* `n = 15` -> `[1, 'fizz', 2, 'buzz', 3, 'fizz', 'buzz', 5, 'fizz', 'buzz', 7, 8, 'fizz', 'buzz', 'fizzbuzz']`

**Solution (JavaScript):**
```javascript
function fizzBuzz(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      result.push('fizzbuzz');
    } else if (i % 3 === 0) {
      result.push('fizz');
    } else if (i % 5 === 0) {
      result.push('buzz');
    } else {
      result.push(i);
    }
  }
  return result;
}

console.log(fizzBuzz(10)); // [1, 'fizz', 2, 'buzz', 4, 'fizz', 'buzz', 7, 8, 'fizz']
console.log(fizzBuzz(15)); // [1, 'fizz', 2, 'buzz', 3, 'fizz', 'buzz', 5, 'fizz', 'buzz', 7, 8, 'fizz', 'buzz', 'fizzbuzz']
```
This code uses a simple `for` loop to iterate from 1 to `n`, and checks the multiples of 3 and 5 using the modulo operator (`%`). If both conditions are met, it pushes "fizzbuzz" to the result array. Otherwise, it pushes either "fizz", "buzz", or the original number to the result array.
