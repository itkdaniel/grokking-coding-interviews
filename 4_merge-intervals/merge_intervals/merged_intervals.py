# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Merge Intervals
##
##   Problem Statement
"""
##   We are given an array of closed intervals, intervals, where each interval 
##   has a start time and an end time. The input array is sorted with respect to 
##   the start times of each interval. For example, intervals 
##   = [[1,4],[3,6],[7,9]] is sorted in terms of start times 1, 3, and 7.
##   Your task is to **merge** the __overlapping_intervals__ and return a new 
##   output array consisting of only the non-overlapping intervals.
##
##   Constraints:
##   * 1 <= intervals.length <= 10^4
##   * intervals[i].length = 2
##   * 0 <= start time <= end time <= 10^4
##
##   Example 1:
##   Input: [[1,5],[3,7],[4,6],[6,8]]
##   Ouput: [1,8]
##   Explanation: Intervals [1,5], [3,7], [4,6], [6,8] are overlapping.
##                Merge them to one interval [1,8].
##   
##   Example 2:
##   Input: [[10,12],[12,15]]
##   Output: [10,15]
##   Explanation: Intervals [10,12],[12,15] are overlapping
##                Merge them to one interval [10,15]
##
##   Example 3:
##   Input: [[1,3],[2,6],[8,10],[15,18],[18,20]]
##   Output: [1,6],[8,10],[15,20]
##   Explanation: Intervals [1,3] and [2,6] overlap and are merged to [1,6].
##                Intervals [15,18] and [18,20] overlap and are merged to [15,20]
##
"""
##   Understand the Problem
"""
##   1. Given the below intervals, find the correct output after merging the 
##      overlapping intervals.
##      Input: [[1,6],[2,4]]
##      Output: [1,6]
##
##   2. Given the below intervals, find the correct output after merging the 
##      overlapping intervals.
##      Input: [[1,8]]
##      Output: [1,8]
##
##   3. Given the below intervals, find the correct output after merging the 
##      overlapping intervals.
##      Input: [[2,9],[3,5],[4,8]]
##      Output: [2,9]
##
##   4. Given the below intervals, find the correct output after merging the 
##      overlapping intervals.
##      Input: [[2,4],[3,5],[4,5],[6,10],[12,14]]
##      Output: [2,5],[6,10],[12,4]
##
"""
##   Arrange the Steps
"""
##   1. Insert the first interval from the input list into the output list.
##   2. Start a loop to iterate over each interval of the input list, except for 
##      the first.
##   3. If the input interval is overlapping (i.e input.start <= output[n].start
##      with the last interval in the output list, merge these two intervals and 
##      replace the last interval of the output list with this merged interval.
##   4. Otherwise, if the input interval does not overlap with the last interval 
##      in the output list, add the input interval to the output list.
##
"""
##   Write the Solution Code (self)
def merge_intervals(intervals: list[list[int]])->list[list[int]]:
    """
    ##   Most Efficient Solution
    ##
    ##   Time Complexity: O(n)
    ##   Space Complexity: O(1)
    ##
    """
    left,right = 0,1
    while right < len(intervals):
        if intervals[right][0] <= intervals[left][1]:
            intervals[left][1] = max(intervals[right][1], intervals[left][1])
        else:
             intervals[left+1] = intervals[right]
             left += 1
        right += 1
    left += 1
    right -= 1
    while right >= left:
        intervals.pop()
        right -= 1
    return intervals

##   Solution Summary
"""
##   The above solution has a time comlexity of O(n), where n is the number of 
##   intervals in the input list. This is because the function has 2 separate 
##   loops that iterate at most the length of the input list. 
##   The first loop manipulates the original input list into a list of the 
##   merged intervals.
##   Then the second loop removes the rest of the intervals that were already 
##   processed, starting from the index of the last merged interval to the end 
##   of the list.
##   
##   The space complexity of the above solution is O(1). This is because the 
##   function manipulates and transforms the original input list into the output 
##   list directly without using any additional data structures.
##
##   Therefore, this is the most efficient solution in terms of time and space 
##   complexity. ✓
"""

def merge_intervals2(intervals: list[list[int]]):
    """
    ##   [[2,4],[3,5],[4,5],[6,10],[12,14]]
    ##   r = [[2,4]]
    ##
    ##   Input: [[1,3],[2,6],[8,10],[15,18],[18,20]]
    ##   Output: [1,6],[8,10],[15,20]
    ##   Explanation: Intervals [1,3] and [2,6] overlap and are merged to [1,6].
    ##                Intervals [15,18] and [18,20] overlap and are merged to [15,20]
    ##   r = [1,6],[8,10],[15,20]
    ##
    ##   overlap: 
    ##      1. out[1] >= in[0]; 
    ##           then o[1] = in[1]
    ##      2. in[0] > out[1];
    ##           then append in[0][1]
    ##           
    ##   [[2,9],[3,5],[4,8]] 
    ##   [[2,9]]
    ##
    """
    """
    ##   6 conditions for overlapping intervals:
    ##      1. - b.start > a.end 
    ##          -> a does not overlap b: a.start < b.start, a.end < b.end
    ##          -> a ends before b
    ##            :: add b to output
    ##      2. - b.start <= a.start and b.end >= a.end 
    ##          -> b >> a: 
    ##            :: merge_interval(a,b) 
    ##                -> c.start = min(a.start,b.start)
    ##                -> c.end = max(a.end,b.end)
    ##      3. - b.start <= a.end and b.end > a.end 
    ##          -> a.start < b.start,a.end <  b.end 
    ##            ::merge_intervals(a,b)
    ##               -> c.start = min(a.start,b.start)
    ##               -> c.end = max(a.end,b.end)
    ##      4. - a.start <= b.start and a.end >= b.end 
    ##          -> a >> b: a.s < b.s, a.e > b.e
    ##            :: merge_intervals(a,b)
    ##               -> c.start = min(a.start,b.start)
    ##               -> c.end = max(a.end,b.end)
    ##      5. - a.start > b.start and a.end > b.end
    ##          -> a > b: a.s > b.s and a.e > b.e
    ##            :: merge_intervals(a,b)
    ##              -> c.start = min(a.start,b.start)
    ##              -> c.end = max(a.end,b.end)
    ##      6. - b.start < a.start and b.end > a.end
    ##          -> a does not overlap b: b.start < a.start, b.end < a.end
    ##          -> b ends before a
    ##            :: add interval to output list
    ##
    ##      1. Common condition for all 6 overlap situation:
    ##          for any 2 intervals that overlap in some way,
    ##          b.start is always less than or equal to a.end,
    ##          (i.e overlap if b.start <= a.end) 
    ##      
    ##      **NOTICE**: For every condition for both overlap or no overlap,
    ##                  the current merged interval is:
    ##                  :: if b.start <= a.end; then
    ##                      the minimum of the start values of a and b.
    ##                      the maximum of the end values of a and b 
    ##                      [min(a.start,b.start), max(a.end,b.end)]
    ##                     else:
    ##                      append b to output
    ##              
    ##                                                a       
    ##              Example: [[1,3],[2,6],[8,10],[15,18],[18,20]]
    ##                                                    b
    ##                      c = [min(a[0],b[0]),max(a[1],b[1]]
    ##                        = [1,6],[8,10],[15,20]
    """
    merged_intervals = [intervals[0]]
    for i in range(1,len(intervals)):
        # n = len(output)
        if intervals[i][0] <= merged_intervals[-1][1]:
            # start time overlaps with current end time
            # update the new end time as current intervals start time
            merged_intervals[-1][1] = max(intervals[i][1],merged_intervals[-1][1])
        else:
            merged_intervals.append(intervals[i])
    return merged_intervals

from collections import deque
def merge_intervals2(intervals: list[list[int]])->list[list[int]]:
    merged = [intervals[0]]
    for interval in range(1,len(intervals)):
        merged[-1].__setitem__(1, max(intervals[interval][1], merged[-1][1])) \
                                    if intervals[interval][0] <= merged[-1][1] \
                                    else merged.append(intervals[interval])
    return merged

def merge_intervals3(intervals):
    intervals = deque(intervals)
    merged = [intervals.popleft()]
    while intervals:
        interval = intervals.popleft()
        merged[-1].__setitem__(1,max(interval[1], merged[-1][1])) \
                        if interval[0] <= merged[-1][1] \
                        else merged.append(interval)
    return merged

##   Solution Summary
"""
##   1. Insert the first interval fromthe input list into the output list.
##   2. Traverse the input list of intervals. For each interval in the input 
##      list, we do the following:
##      1. If the input interval is overlapping 
##         (i.e input[i].start <= output[-1].start), then merge these two 
##         intervals by replacing the end time of the last interval in the 
##         output list, with the end time of the current input interval.
##      2. Otherwise, there is no overlap, add the the input interval to the 
##         output list containing the merged intervals.
"""
##   Time Complexity
"""
##   The time complexity of the above solution is O(n), where n is the number of 
##   intervals. Other built-in Python functions used such as max() have a time 
##   complexity of O(1). Therefore, the final time complexity/runtime of this 
##   algorithm is O(n).
##
"""
##   Space Complexity
"""
##   The space complexity of the above solution is O(n), where n is the number 
##   of intervals. This is because it creates an additional array/list data 
##   structure to store the result of merged_intervals. Built-in Python 
##   functions such as max() is O(1), and do not affect the overall 
##   complexity. Therefore, the final space complexity is O(n).
##
"""
