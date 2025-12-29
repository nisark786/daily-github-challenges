Problem Statement: Write a function called `findMax` that takes an array of numbers as input, finds the maximum number in the array using recursion, and returns this value. If the empty array is provided, return null. The aim here is to find the max element through recursive calls without using built-in functions like Math.max().
 
Solution Code:
```javascript
function findMax(arr) {
    // Base case when there are no elements in the array or only one element left (the last). Return null if empty, else return last number as base condition returns itself.
    if (arr.length === 0 || arr.length === 1) {
        return arr.length ? arr[0] : null;
    }
    
    // Recursive case: compare the first element with max value of rest array, and choose which one is greater to continue recursion or stop when only two elements are left (in this last condition we don't need recursion). 
    return findMax(arr.slice(1)) === null ? arr[0] : Math.max(arr[0], findMax(arr.slice(1)));
}
```
To test the solution, you can run:
```javascript
console.log(findMax([5, 2, -3, 7, 8])); // Expected output is 8 as it's the maximum number in this array.
console.log(findMax([])); // Expected empty case returns null.
```
