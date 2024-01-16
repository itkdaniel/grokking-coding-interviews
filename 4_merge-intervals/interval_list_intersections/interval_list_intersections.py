# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Interval List Intersections
##
##   Problem Statement
"""
##   For two lists of closed intervals given as input, interval_list_a and 
##   interval_list_b, where each interval has its own start and end time, write 
##   a function that returns the intersection of the two interval lists.
##
##   For example, the intersection of [3,8] and [5,10] is [5,8].
##
##   Constraints:
##   * 0 <= interval_list_a, interval_list_b <= 1000
##   * 0 <= start[i] < end[i] <= 10^9, where i is used to indicate interval_list_a
##   * end[i] < start[i+1]
##   * 0 <= start[j] < end[j] <= 10^9, where j is used to indicate interval_list_b
##   * end[j] < start[j+1]
##
##   Example 1:
##   Input: a = [[1,4],[5,6],[7,9]], b = [[3,5],[6,7],[8,9]]
##   Output: [[3.4],[[5,5],[6,6],[7,7]],[8,9]]
##
##   Example 2:
##   Input: a = [[0,4],[5,7],[8,12],[13,15],[16,18]], b = [[0,18]]
##   Output: [[0,4],[5,7],[8,12],[13,15],[16,18]]
##
"""
##   Understand the Problem
"""
##   Objective: Find te crossing points between the two lists a and b
##   Example: a = [2,6], b = [1,4] 
##            x_point = 
##   1. From the following interval lists, find their intersecting intervals.
##   Input: a = [[2,6],[7,9],[10,13],[14,19],[20,24]],
##          b = [[1,4],[6,8],[15,18]]
##   Output: [[2,4],[6,6],[7,8],[15,18]]
##
##     |--1----2----3----4----5----6----7----8----9----0----1----2----3----4----5----6----7----8----9----|
##   a [       2-------------------6    7---------9    0--------------3    4------------------------9    ]
##   b [  1--------------4         6---------8                                  5--------------8
##   r [       |---------|        |-|   |----|                                  |--------------|         ]
##             [2       4]        [6]   [7  8]                                  [15          18]
##   
##   2. From the following interval lists, find their intersecting intervals.
##   Input: a = [[1,29]], 
##          b = [[1,5],[6,10],[11,14],[15,18],[19,20]]
##   Output: [[1,5],[6,10],[11,14],[15,18],[19,20]]
##     |__1__2__3__4__5__6__7__8__9__0__1__2__3__4__5__6__7__8__9__0__1__2__3__4__5__6__7__8__9__|
##   a [  1-----------------------------------------------------------------------------------9
##   b [  1-----------5  6-----------0  1--------4  5--------8  9--0                          ]
##   r [  [1----------5] [6         0]  [1      4]  [5      8]  [90]  ]
##   
"""
##   Arrange the Steps
"""
##   1. Set two pointers, i and j at the beginning of both lists, respectively, 
##      for iteration.
##   2. While iterating, find the latest starting time and earliest ending time 
##      for each pair of intervals [arr_a[i],arr_b[j]].
##   3. If the latest starting time is less than or equal the earliest ending 
##      time, store it as an intersection in an output list containing the
##      intersections.
##   4. Increment the pointer, either i or j, of the list which has the smaller 
##      ending time for the current interval.
##   5. Keep iterating and repeat the steps 2-4 until either list is fully 
##      traversed/processed.
##   6. Return the list of intervals.
##
"""
##   Write the Solution Code
def intervals_intersection(intervals_a, intervals_b):
    """
    ##     |-1-2-3-4-5-6-7-8-9-|
    ##   a [ 1-----4 5-6 7---9 ]
    ##   b [     3---5 6-7 8-9 ]
    ##   c [ [3,4]
    ##      [[1,4],[5,6],[7,9]]
    ##                   ^
    ##      [[3,5],[6,7],[8,9]]
    ##                    ^
    ##      i,j = 2,2
    ##      c = [[3,4],[5,5],[6,6],[7,7],[8,9]]
    ##
    ##     |-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-|
    ##   a [   2-------6 7---9 0-----3 4---------9 0-------4 ]
    ##   b [ 1-----4   6---8             5-----8             ]
    ##   c [ 
    ##     [[2,6],[7,9],[10,13],[14,19],[20,24]]
    ##             ^
    ##     [[1,4],[6,8],[15,8]]
    ##                   ^
    ##      i,j = 1,2
    ##      c = [[2,4],[6,6],[7,8],[15,8]]
    """
    i,j = 0,0
    intersections = []
    while i < len(intervals_a) and j < len(intervals_b):
        max_start = max(intervals_a[i][0], intervals_b[j][0])
        min_end = min(intervals_a[i][1], intervals_b[j][1])
        if max_start <= min_end:
            if intervals_a[i][1] <= intervals_b[j][1]:
                i += 1
            else:
                j += 1
            intersections.append([max_start,min_end])
        else:
            if intervals_a[i][0] <= intervals_b[j][0]:
                i += 1
            else:
                j += 1
    return intersections

##   Naive Approach
"""
##   The naive approach uses a nested loop for finding intersecting intervals.
##    * The outer loop iterates for every interval in interval_list_a and the 
##      inner loop will search for any intersecting interval in the 
##      interval_list_b.
##    * If any interval in list b intersects with the current interval of list 
##      a, we add it to the intersections list.
##   The time complexity for this naive approach will be O(n^2) since we are 
##   using nested loops.
"""
##   Solution Summary
"""
##   Since both arrays are sorted, we can safely compare pairs of intervals, one 
##   from each interval list (i.e interval_list_a[i],interval_list_b[j]), 
##   knowing that after each comparison, we don't need to backtrack and re-check 
##   either list from the start, and can move forward in the lists.
##
##   Therefore, the optimized algorithm is:
##   1. Set two pointers, i and j, at the beginning of each list, respectively, 
##      for iteration.
##   2. While iterating, find the latest starting time and earliest ending time 
##      for each pair of intervals [a[i],b[j]].
##   3. If the latest starting time is less than or equal to the ealiest ending 
##      time, store it in the intersecting intersections output list.
##   4. Increment the pointer of the list that has the smaller end time of the 
##      current interval.
##   5. Else, if the latest starting time is greater than earliest ending time, 
##      then increment the pointer of the list that has the smaller starting 
##      time.
##   6. Continue iterating and repeating steps 3-5 until either list is fully 
##      traversed.
##   7. Return the list of intersections.
##   
"""
##   Time Complexity
"""
##   The time complexity of the function is O(n+m), where n is the length of 
##   interval_list_a and m is the length of interval_list_b. 
##   This is because we iterate through both lists simultaneously using two 
##   pointers, and the number of iterations is determined by the length of the 
##   lists. The max and min functions used to calculate the start and end times 
##   have a time complexity of O(1) as they operate on constant-sized inputs.
##
"""
##   Space Complexity
"""
##   The space complexity of the solution function of Interval List 
##   Intersections is O(1) because the function only uses a constant amount of 
##   extra space to store the intersecions. The space complexity of the built-in 
##   Python functions invoked by the code is not considered in this analysis.
##
"""
