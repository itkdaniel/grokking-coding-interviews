# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Employee Free Time
##
##   Problem Statement
"""
##   You're given a list containing the schedules of multiple employees. Each 
##   person's schedule is a list of non-overlapping intervals in sorted 
##   order. An interval is specified with the start and end time, both being 
##   positive integers. Your task is to find the list of finite intervals 
##   representing the free time for all the employees.
##
##   Constraints:
##   * 1 <= schedule.length,schedule[i].length <= 50
##   * 0 <= interval.start < interval.end < 10^8, where interval is any interval 
##                                                in the list of schedules
##   Example 1:
##   Input: a = [[1,2],[5,6]], b = [[1,3]], c = [[4,10]]
##   Output: [[3,4]]
##   Explanation: 3:00 - 4:00 is the common free interval (finite), 
##   [-inf,1],[10,inf] are also common free intervals but they contain inf and 
##   are not finite.
##
##   Example 2:
##   Input: a = [[1,3],[6,7]], b = [[2,4]], c = [[2,5],[9,12]]
##   Output: [[5,6],[7,9]]
##
##   Example 3:
##   Input: a = [[2,3],[7,9]], b = [[1,4],[6,7]]
##   Output: [[4,6]]
##
"""
##   Understand the Problem
"""
##   1. From the given list of employee schedules, find the list of intervals 
##      representing the free time for all the employees.
##      Input: [[[3,5],[8,10]], [[4,6],[9,12]], [[5,6],[8,10]]]
##      :: Output: [[6,8]]
##
##   2. From the given list of employee schedules, find the list of intervals 
##      representing the free time for all the employees.
##      Input: [[[1,3],[5,6],[9,10]], [[2,4],[7,8]], [[8,11],[12,14]]]
##      :: Output: [[4,5],[6,7],[11,12]]
##
##   3. From the given list of employee schedules, find the list of intervals 
##      representing the free time for all the employees.
##      Input: [[[1,2],[3,4]], [[2,3]], [[4,6]]]
##      :: Output: []
##
"""
##   Arrange the Steps
"""
##   1. Initialize a heap and push the first interval of each employee onto the 
##      heap.
##   2. Set the previous interval as the start time of the first interval.
##   3. Repeatedly pop the smallest interval from the heap and compare it with 
##      the previous interval.
##   4. If the current starting time is greater than the previous interval, add 
##      it to the result list.
##   5. Update the previous interval as the maximum of the previous interval and 
##      end time of the current interval.
##   6. Push additional intervals of the current employee onto the heap if it 
##      exists.
##   7. When the heap becomes empty, return the result list.
##
"""
##   Solution Summary
"""
##   Find all common free time intervals by **merging** all intervals and 
##   determine if any gaps or intervals exist between the interval times (slots)
##
##   Variables Used:
##    - previous: to store ending time of previously processed interval (time slot)
##    - i: stores employee's index value
##    - j: stores index into the employee's list of intervals
##    - result: stores the common free time intervals
##   
##   Algoritm Steps:
##    1. Store start time of each employee's first interval along with its index 
##       value and a valiue 0, i.e (schedule[i][0][0],j,0), into a min heap.
##    2. Set a variable, previous_start, to the start time of the first interval 
##       in the min heap
##    3. Then iterate using a loop until the heap is empty, in each iteration:
##      - Pop element from min_heap, set (curr,i,j) to the popped element.
##      - Select the interval from input located at position (i,j) from.
##      - If the selected interval's start time is greater than the previous end 
##        time, it means the time from the previous interval's start time to the 
##        selected interval's start time is free. Add this interval to the 
##        output, result list.
##      - Then, update value of previous start time as max(previous,curr_selected_end)
##      - If the current employee has additional intervals, push it to the min  heap
##   4. After iterations are complete, when the heap becomes empty, return the 
##      output list containing the common free time intervals.
##
##   Example:
##   input = [[[2,3],[7,9]], [[1,4],[6,7]]]
##   :: emp_a = [[2,3],[7,9]]
##                      ^
##      emp_b = [[1,4],[6,7]]
##                      ^
##      heap = []
##      curr = (7,0,1)
##      prev = 9
##      output = [[4,6]]
"""
##   Write the Solution Code
class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.closed = True # Set the interval as closed/open 
                           # (By default, the interval is closed)
    def set_closed(self,closed):
        self.closed = closed
    def __str__(self):
        return f'[{str(self.start)}, {str(self.end)}]' if self.closed \
                else f'({str(self.start)}, {str(self.end)})'

import heapq
def employee_free_time(schedule):
    """
    ##   Input: [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
    ##   emp_a = [[1,3],[6,7]], 
    ##   emp_b = [[2,4]], 
    ##   emp_c = [[2,5],[9,12]]
    ##   Output: [[5,6],[7,9]]
    ##   
    ##     <----1----2----3----4----5----6----7----8----9----10----11----12---->
    ##   a [   1---------3              6----7                                ]
    ##   b [        2---------4                                               ]
    ##   c [        2--------------5                   9----------------12    ]
    ##   x [                      [5----6]   [7---------9] 
    ##   heap = []
    ##   
    ##     <----1----2----3----4----5----6----7----8----9----10----11----12---->
    ##   a [         2----3                   7---------9                      ] 
    ##   b [    1--------------4         6----7                                ]
    ##   x [ 
    ##
    ##   Input: [[[2,3],[7,9]], [[1,4],[6,7]]]
    ##                                  ^
    ##   emp_a = [[2,3],[7,9]]
    ##   emp_b = [[1,4],[6,7]]
    ##
    ##   prev_int = 7
    ##   heap = [[7,9]]
    ##   pop = [6,7]
    ##   r = [[4,6]]
    """
    output = []
    heap = []
    for i in range(len(schedule)):
        heapq.heappush(heap,(schedule[i][0],i,0))
    prev_start_time = heap[0][0][0]
    while heap:
        curr,curr_emp,sched_index = heapq.heappop(heap)
        if curr[0] > prev_start_time:
            output.append([prev_start_time,curr[0]])
        prev_start_time = max(curr[1], prev_start_time)
        if sched_index+1 < len(schedule[curr_emp]):
            heapq.heappush(heap,(schedule[curr_emp][sched_index+1],curr_emp,sched_index+1))
    return output

##   Time Complexity
"""
##   The time complexity of the solution function for Employee Free Time is 
##   O(n log m), where n is the total number of intervals across all employees 
##   and m is the number of employees. This is because we iterate through each 
##   interval in the schedule and perform heap operations, which have a time 
##   complexity of O(log m). The heapq module is also used to perform heap 
##   operations, which also has a time complexity of O(log m).
##
"""
##   Space Complexity
"""
##   The space complexity of the solution function for Employee Free Time is 
##   O(n), where n is the number of intervals across all employees. This is 
##   because we use a heap to store the intervals, which requires O(n) 
##   space. The output list also requires O(n) space in the worst case if there 
##   are no overlapping intervals. The space complexity of the built-in Python 
##   functions used such as heapq.heappush and heapq.heappop is O(log n), where 
##   n is the number of elements in the heap.
##
"""
