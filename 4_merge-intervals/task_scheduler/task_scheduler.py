# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Task Scheduler
##
##   Problem Statement
"""
##   We're given a character array, tasks, where each characer represents 
##   a unique task. These tasks need to be performed by a single CPU, with each 
##   task taking one unit of time. The tasks can be performed in any order. At 
##   any given time, a CPU can either perform some task or stay idle.
##
##   For the given tasks, we are also provided with a positive integer value, n, 
##   which represents the cooling period between any two identical tasks. This 
##   means that the CPU must wait for at least n units of time before it 
##   performs the same task again. For example, if we have the tasks [A,B,A,C] 
##   and n = 2, then after performing the first A task, the CPU will wait for at 
##   least 2 units of time to perform the second A task. During these 2 units of 
##   time, the CPU can either perform some other task or stay idle.
##
##   Given the two input values, tasks and n, find the least number of units of 
##   time the CPU will take to perform the given tasks.
##
##   Constraints:
##   * 1 <= tasks.length <= 1000
##   * tasks consists of uppercase English letters
##   * 0 <= n <= 100
##
##   Example 1:
##   input: tasks = [A,A,B,B], n = 2
##   output: [A,B,None,A,B]
##           units_of_time = 5
##   
##   Example 2:
##   input: tasks = [A,B,A,A,B,C], n = 3
##   output: [A,B,C,None,A,B,None,None,A]
##
##   Example 3:
##   input: tasks = [A,C,B,A], n = 0
##   output: [B,A,C,A], units_of_time = 4
##     **Note**: Here, we can have any permutation of size 4 since n = 0.
##               For example: [A,B,C,A],[A,B,A,C],[B,C,A,A],[C,B,A,A],[A,A,C,B]
##
"""
##   Understand the Problem
"""
##   1. What is the minimum number or units of time if the following values are 
##      given as input?
##      Input: tasks = [A,A,A,B,B,C,C], n = 1
##      :: Output = [A,B,C,A,B,C,A] units_of_time = 7
##   2. Choose the correct final schedule if the following values are 
##      given as input?
##      Input: tasks = [D,A,F,B,G,E,C], n = 5
##      :: Output: [D,A,F,B,G,E,C], units_of_time = 8
##
##   3. What is the minimum number or units of time if the following values are 
##      given as input?
##      Input: tasks = [A,A,C,C,C,B,E,E,E], n = 2
##      :: Output: [E,C,A,E,C,A,E,C,B], units_of_time = 9
##
"""
##   Arrange the Steps
"""
##   1. Count and store the frequencies of all the tasks.
##   2. Sort them in descending order.
##   3. Iterate through the tasks and schedule them in descending order of 
##      frequencies and compute the idle time.
##   4. The total time can be calculared as the sum of number of tasks and idle 
##      time.
##
"""
##   Write the Solution Code
from collections import Counter   
def least_time(tasks: list[str], n: int)->int:
    task_freq = Counter(tasks)
    task_freq = dict(sorted(task_freq.items(), key=lambda x: -x[1]))
    max_freq = task_freq.popitem()[1]
    idle_time = (max_freq - 1) * n
    while task_freq and idle_time > 0:
        idle_time -= min(max_freq - 1, task_freq.popitem()[1])
    idle_time = max(0, idle_time)
    return len(tasks) + idle_time

