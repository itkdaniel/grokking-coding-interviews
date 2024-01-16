# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Meeting Rooms II
##
##   Problem Statement
"""
##   We are given an array of meeting time intervals, intervals, where each 
##   interval has a start time and an end time. Your task is to find the minimum 
##   number of meeting rooms required to hold these meetings.
##
##   An important thing to note here is that the specified end time for each 
##   meeting is exclusive.
##
##   Constraints:
##   * 1 <= intervals.length <= 10^3
##   * 0 <= start[i] < end[i] <= 10^5
##
##   Example 1:
##   Inputs: [[2,8],[3,4],[3,9],[5,11],[8,20],[11,15]]
##   Output: 3
##   Explanation: room_1 = [[2,8],[8,20]], room_2 = [[3,4],[5,11]], 
##                                          room_3 = [[3,9],[11,15]]
##
##   Example 2:
##   
"""
##   Arrange the Steps
"""
##   1. Sort the given input intervals with respect to their start times.
##   2. Initialize a min_heap and push the first interval's end time onto the 
##      heap.
##   3. Loop over the remaining intervals.
##   4. In each iteration, compare the start time of the current interval with 
##      all end times present in the heap.
##   5. If the earliest end time of all intervals seen so far (the root of 
##      min_heap) occurs before the start time of the current interval, remove 
##      the earliest interval from the heap and push the current interval onto 
##      the heap.
##   6. Otherwise, allot a new meeting room, that is, add the current interval 
##      in the heap without removing any existing interval.
##   7. After processing all the intervals, the size of the heap is the count of 
##      meeting rooms needed to hold the meetings.
##
"""
##   Write the Solution Code
##   *hint*: The optimal solution runs in O(n log n) time and O(n) space.
import heapq
def find_sets(intervals):
    output = []

    return output
