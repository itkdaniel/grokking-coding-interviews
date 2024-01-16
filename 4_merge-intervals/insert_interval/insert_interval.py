# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Insert Interval
##
##   Problem Statement
"""
##   Given a sorted list of nonoverlapping intervals and a new interval, your 
##   task is to insert the new interval into the correct position while ensuring 
##   that the resulting list of intervals remains sorted and 
##   nonoverlapping. Each interval is a pair of nonnegative numbers, the first 
##   being the start time and the second being the end time of the interval.
##
##   Constraints:
##   * 0 <= existing_intervals.length <= 10^4
##   * existing_intervals[i].length, new_interval.length == 2
##   * o <= start time, end time <= 10^4
##   * The first number should always be less than the second number in each 
##     interval.
##   * The list of intervals is sorted in ascending order based on the first 
##     element (i.e start time) in every interval.
##
##   Example 1:
##   Inputs: [[1,3],[5,7],[8,9],[10,13]], [[2,6]]
##   Output: [[1,7],[8,9],[10,13]]
##   Explanation: First, merge [2,6] with the first interval [1,3], creating 
##   [1,6]. Then merge [1,6] with the next overlapping interval, [5,7], creating 
##   [1,7]. Intervals [8,9] and [10,13] don't overlap with any intervals, so 
##   they will stay independently.
##
##   Example 2:
##   Input: [[1,3],[6,9]], [[2,5]]
##   Output: [[1,5],[6,9]]
##   Explanation: First, merge [2,5] with [1,3], creating [1,5].Then [6,9] does 
##   not overlap so it will stay independent.
##
"""
##   Understand the Problem
"""
##   1. What will be the updated list of intervals?
##      Input: [[1,3],[4,5],[7,8],[9,12],[13,14]], [2,10]
##      :: Output: [[1,12],[13,14]]
##   2. What will be the updated list of intervals?
##      Input: [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
##      :: Output: [[1,2],[3,10],[12,16]]
##   3. What will be the updated list of intervals?
##      Input: [[1,2],[5,7],[8,10]], [3,4]
##      :: Output: [[1,2],[3,4],[5,7],[8,10]]
##   4. What will be the updated list of intervals?
##      Input: [[3,5]] 
##      :: Output: [[1,10]]
##


##   [[1,3],[5,7],[8,9],[10,13]], [[2,6]]
##   [[1,7],[8,9],[10,13]]
##
##   [[1,3],[6,9]], [[2,5]]
##   [[1,5],[6,9]]
##
##   [[1,3],[4,5],[7,8],[9,12],[13,14]], [[2,10]]
##   [[1,12],[13,14]]
##
##   [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
##   [[1,2],[3,10],[12,16]]
##
##   [[1,2],[5,7],[8,10]], [3,4]
##   [[1,2],[3,4],[5,7],[8,10]]
##
##   [[3,5]], [1,10]
##   [[1,10]]
##
"""
##   Arrange the Steps
"""
##   1. Iterate the input list of intervals until reaching the end of input.
##   2. In each iteration, compare the new interval with the interval at the 
##      latest merged interval in the input list.
##   3. If the start value of the new interval is less than or equal to the end 
##      value of the latest merged interval, update and merge the new interval 
##      with the latest merged interval.
##   4. If the new interval does not overlap with the latest merged interval
##   5. check if the start value of the new interval is less than the start of 
##      the latest merged interval, or greater than the end of the latest merged 
##      interval:
##      - if new.start is < latest.start, insert the new interval to the 
##      position just before the latest merged interval
##      - if new.start > latest.end, insert the new interval to the position 
##      after the latest interval
##   6. Return the output of the merged intervals.
##
"""
"""
##   1. Iterate through the existing intervals and append all intervals 
##      occurring befre the new interval to the output list.
##   2. Check if there is an overlap between the last interval in the output·
##      list and the new interval.
##   3. If there is an overlap, merge them by updating the end value of the last·
##      interval in the output list to the maximum of the current interval end·
##      time and the new interval end time.
##   4. Otherwise, append the new interval to the output list
##   5. Continue iterating through the remaining intervals and merge any 
##      overlapping intervals with the last interval in the output list.
##   6. Return the final output list containing the merged intervals.
##
"""
##   Write the Solution Code
def insert_interval(existing_intervals, new_interval):
    """
    ##   *********************************************************************
    ##   **                                                                 **
    ##   **     TODO:                                                       **
    ##   **     Optimize by storing the output as a linked list or heap     **
    ##   **                                                                 **
    ##   *********************************************************************
    ##
    ##   Sample Input #1: [[1,2],[5,7],[8,10]], [3,4]
    ##
    ##   Sample Input #2: [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
    """
    merged_intervals = []
    for i in range(len(existing_intervals)):
        if existing_intervals[i][0] <= new_interval[0]:
            merged_intervals.append(existing_intervals[i])
        else:
            if new_interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(new_interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1],new_interval[1])
        if existing_intervals[i][0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(existing_intervals[i][1],merged_intervals[-1][1])
        else:
            merged_intervals.append(existing_intervals[i])
    if len(merged_intervals) == len(existing_intervals):
        if new_interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][0] = min(merged_intervals[-1][0],new_interval[0])
            merged_intervals[-1][1] = max(merged_intervals[-1][1],new_interval[1])
    else:
        if existing_intervals[-1][0] <= merged_intervals[-1][1]:
            merged_intervals[-1][0] = min(merged_intervals[-1][0],existing_intervals[-1][0])
            merged_intervals[-1][1] = max(merged_intervals[-1][1],existing_intervals[-1][1])
        else:
            merged_intervals.append(existing_intervals[-1])
    return merged_intervals

##   Solution Summary
"""
##   1. Append all intervals occurring before the new interval to the output 
##      list until reaching an interval that starts after the starting point of 
##      the new interval.
##   2.  After all intervals occurring before the new interval have been added 
##       to the output list, check if there is an overlap between the last 
##       interval in the output list and the new interval.
##        - If there is an overlap, merge the end times of the last interval in 
##          the output list and the new interval.
##        - Otherwise, add the new interval to the output list
##   3. Continue iterating through the remaining existing intervals and merge 
##      the overlapping intervals with the last interval in the output list.
##   4. After iteration of the input list is complete, check if the length of 
##      the output list equals to the length of the input list and either add 
##      the last interval from the input list or the new interval to the output 
##      list, or merge them if there is an overlap.
##   5. Return the output list containing the merged intervals
"""
##   Time Complexity: O(n)
"""
##   The time complexity of the above solution is O(n), where n is the number of 
##   intervals in the input list, existing_intervals.
##   This is because the function iterates through each interval in the list at 
##   most once.
##   The time complexity of the built-in Python functions used such as append(), 
##   max(), min(), are all O(1) as they use a constant number of elements.
##
"""
##   Space Complexity: O(n)
"""
##   The space complexity of the above solution is O(n), where n is the number 
##   of intervals in the input list, existing_intervals.
##   This is because the function uses an additional list, merged_intervals, to 
##   stre the merged intervals. The size of merged_intervals can be at most n+1, 
##   as a new interval may be inserted at the end. The spsace complexity of the 
##   built-in Python functions used such as append() and max(), are also 
##   constant and does not contribute significantly to the overall space 
##   complexity. 
##
"""
