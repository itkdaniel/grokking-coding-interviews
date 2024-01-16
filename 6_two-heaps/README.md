# vim: set comments=sb\:\*,sb\:\ \ \ \*,mb\:\ \ \ -,ex-3\:\*,\:>,fb\:\*,fb\:-,\:»,fb\:»:
# vim: set fo=tcqrowpn:
# vim: set tw=120:

# Two Heaps

## Examples
The following are examples of problems that can be solved using the Two-Heap
approach.

### Find the median of all windows of length k in the array
Use two heaps, small list (max-heap), and large list (min-heap), to store the
elements of the window. We want to store the numbers larger than the median in a
large list, and smaller ones in small list. The medians array will store the
median of each window.

```
Array : [ 3, 1, 2, -1, 0, 5 ,8, __k__, 4 ]
        [ Small List ]  [ Large List ] 
Small List: 
			3
   1    2
-1
medians

Small List:
    1
  /
-1
Medians: 1.5

Large List:
       
      1   
     /  \
    3    2 
Medians: 1.5, 0.5
```

### Find the maximum remaining capital from selecting at most k projects
The __capitals__ array contains the capital required to complete each project.
The __profits__ array contains the profit obtained from each project. The
variable __c__ represents our starting capital.

We will use a min-heap, __min_capitals__ to store the capitals, and a max-heap,
__max_profits__, to store the profits. The variable __available_capital__
(initialized to c) represents our current capital.

1. Initial Step: We first add all the elements of the capitals array to
	 min profits in pairs of the following form: (capitals[i], i)
2. Iterative Step: To shortlist the projects we can potentially select from our
	 available capital, we check the top of the min capitals heap to check if it
contains a project having a capital requirement less than, or equal to available
capital. If it does, we pop this project from min capitals and add its
corresponding profit to max profits as a pair: (profits[i], i). We repeat this
process until the top of min capitals contains a capital greater than our
available capital.

__Example__:
c = 2, k = 3

__Min_Capitals__:
capitals = [1, 2 ,3]

__Max_Profits__:
profits = [1, 3, 4]

__Available_Capital__:
availableCapital = 2

## Does the Problem match this Pattern?
* **Yes**: if both these conditions are fulfilled:
	- We need to repeatedly calculate two maxima, two minima, or one maximum and
	  one minimum, based on a changing set of data.
	- The input data is not sorted
* **No**: if any of these conditions are fulfillde:
	- We don't need to track two extreme values (minima or maxima), but only one.
	- When we don't need to repeatedly calculate the extreme values (minima or
	  maxima), but only need to calculate it a fixed number of times.
	- The input data is already sorted - in which case, there is no benefit to
	  using heaps.

## Real-World Problems
* **Video Streaming**: During a user session, there is often a possibility that
  packet drops and buffering might occur. We want to record the median number of
buffering events that might occur in a particular session, which could then be
used to improve the user experience.

* **Netflix**: As part of a demographic study, we're interested in the median
  age of our viewers. We want to implement a functionality whereby the median
age can be updated efficiently whenever a new user signs up for video streaming.

## Match the Problem to the Strategy
1. Find the difference between the maximum and minimum elements in each window
	 of size 4 as it slides through the array, [4,1,2,4,6,8].
	:: Two-Heaps Approach

__Explanation__: By maintaining two heaps, one max-heap and one min-heap, we can efficiently track the maximum and minimum elements within the sliding window. As the window moves through the array, we can quickly update the heaps and compute the difference between their root elements to obtain the desired result for each window.

2. Sort the characters of the given string by frequency.
	:: Some other pattern

3. Find the medians of subarrays of size 3 in the array [1,3,-1,-2,5,3]
	:: Two-Heaps Approach

__Explanation__: 
The Two Heaps pattern involves using two heaps, a max-heap, and a min-heap, to maintain the sorted order of elements. By dividing the subarrays into three elements, we can keep track of the medians efficiently by balancing the elements between the two heaps, enabling us to access the median in constant time without the need for sorting the subarrays.

4. Given the string "hellocodingking", find the longest substring with 5
	 distinct characters.
	:: Some other Approach (Sliding Window)
