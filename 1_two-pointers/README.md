# Two Pointers
The **two pointers** pattern uses two pointers to iterate over one or more array(s) or list(s) until the conditions of the problem are satisfied. 
* This is useful bc it allows us to keep track of the values of two different indexes in a *single* iteration.

Whenever there's a ***requirement to find two data elements*** in an array that satisfy a certain condition, the two pointers pattern should be the first strategy to come to mind.

The pointers can be used to iterat the data structure in one or both directions. For example, to identify whether a string is a palindrom, we can use one pointer to iterate the string from the beginning and the other to iterate it from the end. At each step, we can compare the values of the two pointers and see if they meet the palindrome properties.

The naive approach to solving this problem would be using *nested loops*, with a time complexity of *O(n^2)*. However, by using two pointers moving towards the middle from either end, we exploit the symmetry property of palidromic strings. This allows us to compare the elements in a single loop, making the algorithm more efficient with a time complexity of *O(n)*.


**Here's how the pointers will move along the string**:
```
           v             v
[a b c c b a]   [a b c c b a]
 ^                 ^
       v
[a b c c b a]
     ^
```
> **Essentially**, the two pointers pattern is an application of the ***prune-and-search*** strategy, in which, at every step, we're able to safely prune - that is, eliminate - a set of possible solutions.

## Examples
The following problems illustrate some examples of problems that can be solved with the **two-pointer** approach:
1. Reversing an Array
***v*** **v** *v* *v* **v**         ***v***         
1 2 3 4 5 6  --->  reversed| 6 5 4 3 2 1
2. Pair with Given Sum in a Sorted Array
p1 -------p2
==4== 5 6 7 8 ==9==   ---> target = 11
p1-----p2
==4== 5 6 7 ==8== 9  ---> pair = [4, 7]
p1 ---p2
==4== 5 6 ==7== 8 9

## Does My Problem Match this Pattern?
* **==Yes==**, if all of these conditions are fulfilled:
    - The input data ***can be traversed in a linear fashion***, that is, it's in an array, in a linked list, or in a string of characters.
    - We ***limit our focus to a specific range of elements*** within the input data, as dictated by the positions of the *two* pointers, allowing us to consider a small subset of elements rather than the entire set.

> Additionally, problems in this pattern usually involve comparing or swapping values pointed to by two indexes. In less common cases, each index may move along a separate array or string.

* **==No==**, if either of these conditions is fulfilled:
   - The input data ***cannot be traversed in a linear fashion***, that is, it's neither in an array, nor in a linked list, nor in a string of characters.
   - The problem ***requires an exhaustive search*** of the solution space, that is, eliminating one solution does not eliminate any others.

## Real-World Problems
Many problems in the real world use the two pointers pattern, such as:
* **Memory Management**: Two pointers are vital in memory allocation and deallocation. The memory pool is initialized with two pointers: the **start** pointer, pointing to the beginning of the available memory block, and the **end** pointer, indicating the end of the block. When a process or data structure requests memory allocation, the **start** pointer is moved foward, designating a new memory block for allocation. Conversely, when memory is released (deallocated), the **start** pointer is shifted *backwards*, marking the deallocated memory as available for future allocations.
* **Product Suggestions**: While shopping online, when customers view their cart and the current total doesn't qualify for free shipping, we want to show them pairs of products that can be bough together to make the total amount equal to the amount required to be eligle for free delivery. Two pointers can be used to suggest the pairs that add up to the required cost for free shipping.

### Strategy Samples
Consider the following patterns and their matched strategy
* ==Check if a string is a palindrome== ---> Two Pointers.
By Utilizing two pointers, one starting from the beginning of the string and the other from the end, we can compare the corresponding characters. If the characters match at each step, we continue moving the pointers inward until the pointers cross each other.
* ==Find any 3 values in a sorted array that sum up to 825== ---> Two Pointers
By iterating through the array and considering each value, we calculate the sum of the current value and the other two values. To find the other two values, we can utilize two pointers in each iteration: one starting from the leftmost element and the other from the rightmost element. Comparing this sum with 825, we increment or decrement the pointers accordingly.
* Find all permutations of the following set of elements, {1,2,3}. ---> Some other pattern
Finding permutations requires generating all possible combinations, which involves exploring various branches of a decision tree. This process does not align with the linear traversal approach of the Two Pointers pattern, making it unsuitable for solving permutation problems.
* Generate a string of *n* balanced parentheses. ---> Some other pattern
Generating a string of balanced parentheses requires a different approach, such as backtracking, since it involves forming a specific pattern with nested parentheses. This kind of pattern generation is not supported by the Two Pointers pattern.

## Problems
The following problems illustrate problem solutions that follow the Two Pointers pattern.
1. Valid Palindrome
2. Sum of 3 values
3. Remove nth Node from End of List
4. Sort Colors
5. Reverse Words in a String
6. Valid Palindrom II
