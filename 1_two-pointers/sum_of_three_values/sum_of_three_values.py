# vim: set comments=sl\:\"\"\",m\:##\ \ \ \ ,ex-3\:\"\"\":
# vim: set fo=tcrq :
# vim: set comments=sb\:\"\"\",mb\:##\ \ \ \ ,ex-3\:\"\"\",\:##:
# vim: set fo=tcq1rowabvpn:

##    Problem Statement
"""
##    Given an array of integers, `nums`, and an integer value, `target`, 
##    determine if there are any three integers in `nums` whose sum is equal 
##    to the `target`, that is, `nums[i] + nums[j] + nums[k] == target`.  
##    Return TRUE if three such integers exist in the array. Otherwise, return 
##    False.
##
##    **Note**: A valid triplet consists of elements with distinct indexes.  
##    This means, for the triplet `nums[i],nums[j]`, and `nums[k]`, `i` != `j` 
##    , `i` != `k` and `j` != `k`.
##
##    Constraints:
##    * 3 <= nums.length <= 500
##    * -10^3 <= nums[i] <= 10^3
##    * -10^4 <= target <= 10^4
##
##    Exampe 1:
##    Input: nums = [3,7,1,2,8,4,5], target = 20
##    Output: True
##
##    Example 2:
##    Input: nums = [-1,2,1,4], target = 1
##    Output: False
##
##    Example 3:
##    Input: nums = [-1,2,1,4,-2], target = 1
##    Output: True
##
"""
##    Understand the Problem
"""
##    1. What should be the output if the following set of inputs is provided?
##    nums = [2,3,1], target = 6
##    :: --> True
##    2. What should be the output if the following set of inputs is provided?
##    nums = [1,-1,1], target = 2
##    :: --> False
##    3. What should be the output if the following set of inputs is provided?
##    nums = [1,2,4,6,8,20], target = 31
##    :: --> False
##    4. You are given the following inputs:
##    nums = [1,2,4,6,8,20], target = 31
##    If you could make one replacement in the given array to get to the 
##    target, which replacement would you make?
##    :: --> All of the Above, i.e:                                                                                          
##    --> replace x with y for (x,y) in (2,3),(4,5),(6,7),(20,28)
##
"""
##    Arrange the Steps
"""
##    1. Sort the input array in ascending order.
##    2. Iterate over the entire sorted array to find the triplet whose sum is 
##       equal to the target.
##    3. In each iteration, make a triplet by storing the current array 
##       element and the other two elements using two pointers (low and high), 
##       and calculate their sum.
##    4. Adjust the calculated sum value, until it becomes equal to the target 
##       value, by conditionally moving the pointers, low and high.
##    5. Return TRUE if the required sum is found. Otherwise, return FALSE.
##
"""
##    Write the Solution Code
def find_sum_of_three(nums:list[int], target:int)->bool:
    """
    ##                 
    ##    [3,7,1,2,8,4,5], target = 20
    ##                 v
    ##    [1,2,3,4,5,7,8]
    ##             * ^
    ##    nums.sort()
    ##    i = 0; j = n-1
    ##    k = i+1
    ##    while i < j and j != k:
    ##      if i+j+k < 20 --> i++
    ##      elif ''  > 20 --> j--
    ##      else '' == 20 --> True
    ##      --> False
    ##      [0 1 2 5[0 1 2 5 8] 8]
    """
    i, j = 0, len(nums)-1
    k = i+1
    nums.sort()
    while i < j and j != k:
        num = nums[i]+nums[j]+nums[k]
        if num < target:
            i += 1
        elif num > target:
            j -= 1
        else:
            return True
    return False

##    Solution Sumary
"""
##    First, sort the array in ascending order. To find the triplet whose sum 
##    is equal to the target value, loop through the entire array. In each 
##    iteration:
##      1. Store the initial 3 values i, j, and k where:
##          * i and j represents the indexes for a pair of values where i is 
##          the index of lowest possible value and j is the index of highest 
##          possible value.
##          * k is the index adjacent to i (i.e k=i+1), such that k is a value 
##          that completes a possible triplet.
##          * k is not equal to j, therefore also not equal to i
##     2. Calculate the sum of the array elements pointed to by the current 
##        loop's i, j, and k values.
##     3. Since the array is sorted:
##         * if the sum is less than target, none of the values before the 
##         current index i, can be part of our solution, therefore increment 
##         i, which also increments k to test the next value that possibly 
##         completes the required triplet.
##         * if the sum is greater that target, then none of the values after 
##         the current index j, can be part of our solution, therefore 
##         decrement j, to get a value closer to target.
##         * if the sum is equal to target, return TRUE (triplet found).
##     4. Repeat until the values i, j representing the indexes of the array 
##        cross each other. If i crosses j (i.e i > j), then the entire array 
##        is processed and we don't find any triplet that matches our 
##        requirement, therefore return FALSE.
"""
##    Time Complexity
"""
##    In the solution above, sorting the array takes O(nlog(n)) and the single 
##    loop to find the triplet takes O(n). Here, n is the number of elements 
##    in the input array. Therefore, the total time complexity of this 
##    solution is O(nlog(n) + n), which simplifies to O(n).
"""
##    Space Complexity
"""
##    The space complexity of this solution can range from O(log(n)) to O(n), 
##    as per the sorting algorithm we use. We used the built-in Python 
##    function, sort(), so the space complexity of the provided solution is 
##    O(n).
"""
