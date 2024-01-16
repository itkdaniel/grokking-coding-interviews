# vim: set comments=sb\:\*,sb\:\ \ \ \*,mb\:\ \ \ -,ex-3\:\*,\:>,fb\:\*,fb\:-:
# vim: set fo=tcq1rowpn:
# vim: set tw=0:



###### vim: set comments=s6b\:\ \ \ \*,mb\:\ \ \ \ \ \ -\,ex-3\:\ \ \ \*,\:>,fb\:\*,fb\:-:
# Sliding Window
The **sliding window** pattern is used to process sequential data by maintaining a moving subset of elements, called a window.
## Introduction
The sliding window pattern is aimed at reducing the use of nested loops in an algorithm. It may be viewed as a variation of the two pointers pattern, with the pointers being used to set the window bounds.

A window is a sublist formed over a part of an iterable data structure. It can be used to slide over the data in chunks corresponding to the window size. The sliding window pattern allows us to process the data in segments instead of the entire list. The segment or window size can be set according to the problem's requirements. For example, if we have to find 3 consecutive integers with the largest sum in an array, we can set the window size to 3. This will allow us to process the data 3 elements at a time.

Why is this method more efficient? It isn't if, for each window, we iterate over all the elements of the window because that gives us the same O(kn) time complexity.

Instead, what if we focused on the element entering the window and the one leaving it? For example, after calculating the sum of the first 3 elements, we move the window one step forward, subtract the element that is no longer in the window from the sum, and add the new element that has entered it. Next we check if the new sum is greater than the first. If it is, we update the max sum found so far. Now, each time we move the window forward, we poerform at most **four operations**, reducing the time complexity to O(4n), which is O(n).

## Examples
The following examples illustrate some problems that can be solved with the sliding window approach:
* **Repeated DNA Sequences**: This problem requires a sliding window of size 3, representing a DNA sequence (e.g [A,G,T])
* **Maximum Subarray Sum**: Example: arr = [4,2,8,9,,4,0], subarraySize = 4 
  sum([4,2,8,9]),sum([2,8,9,4]),sum([3,9,4,0]) = 23,23,21 ; MaxSum = 23

## Does My Problem Match This Pattern?
* Yes, if both these conditions are fulfilled:
  - The problem requires repeated computations on a contiguous set of data elements (a subarray or a substring), such that the window moves
    across the input array from on end to the other. The size of the window may be fixed or variable, depending on the requirements of the
    problem. The repeated computations may be a direct part of the final solution, or they may be intermediate steps building up towards the
    final solution.
  - The computations performed every time the window moves take O(1) time or are a slow-growing function, such as log, of a small variable,
    say *k*, where *k << n*.
* No, if either of these conditions are fulfilled:
  - The input data structure does not support random access.
  - You have to process the entire data without segmentation.

## Real-World Problems
Many problems in the real world use the sliding window pattern. Here are some examples:
* **Telecommunications**: Find the maximum number of users connected to a cellular network's base station in every *k*-millisecond sliding 
  window.
* **Ecommerce**: Given a dataset of product IDs in the order they were viewed by the user and a list of products that are likely to be
  similar, find how many time these products occur together in the dataset.
* **Video Streaming**: Given a stream of numbers representing the number of buffering events in a given user session, calculate the median
  number of buffering events in each one-minute interval.
* **Social Media Content Mining**: Given the lists of topics that two users have posted about, find the shortest sequence of posts by one
  user that includes all the topics that the other user has posted about.

## Match the Problem to its Approach
1. Locate the 6th largest element in an array: ==Some other pattern==
   **Explanation**: The Sliding Window approach is primarily used for solving problems that involve *contiguous subarrays* or *sequences 
   within a larger array*. However, finding the 6th largest element requires examining the entire array and comparing multiple elements,
   which does not align with the concept of a sliding window.
2. Given a string find its longest substring that includes 5 distinct characters: ==Sliding Window==
   **Explanation**: By using a window that slides through the string, we can maintain a continous substring and efficiently track te 
   distinct characters within it. As the window expands and contracts, we can update the maximum length of the substring that satisfies
   the condition of having exactly 5 distinct characters.
3. Find 3 contiguous integers in an array with the highest sum: ==Sliding Window==
   **Explanation**: By maintaining a fixed-sized window as we traverse the array, we can continuously update the sum of the integers within 
   the window and keep track of the maximum sum encountered.
4. Find safe places for 5 queens on a 5 x 5 chessboard: ==Some other pattern==
   **Explanation**: The problem of placing 5 queens on a chessboard requires a non-contiguous arrangement, making it incompatible with the
   Sliding Window approach. Alternative approaches, such as backtracking, can be used to solve this problem.
