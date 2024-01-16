# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Minimum Size Subarray Sum
##
##   Problem Statement
"""
##   Given an array of positive integers, nums, and a positive integer, target, 
##   find the minimum length of a contiguous subarray whose sum is greater than 
##   or equal to the target. If not such subarray is found, return 0.
##
##   Constraints:
##   * 1 <= target <= 10^9
##   * 1 <= nums.length <= 10^5
##   * 1 <= nums[i] <= 10^4
##
##   Example 1:
##   Input: nums = [2,3,1,2,4,3], target = 7
##   Ouptut: min_length_subarr = 2, min_subarr = [4,3]
##
##   Example 2:
##   Input: nums = [1,1,1,1,1,3], target = 11
##   Output: min_length_subarr = 0, min_subarr = []
##
##   Example 3:
##   Input: nums = [1,2,7,3,4,5], target = 10
##   Output: min_length_subarr = 2, min_subarr = [7,3]
##   
"""
##   Understand the Problem
"""
##   1. What is the output if the following values are given as input?
##   Input: nums = [1,2,7,1,8], target = 9
##   :: Output: min_length_subarr = 2, min_subarr = [2,7],[1,8]
##
##   2. What is the output if the following values are given as input?
##   Input: nums = [1,3,4,5,2], target = 12
##   :: Output: min_length_subarr = 3, min_subarr = [3,4,5]
##
##   3. What is the output if the following values are given as input?
##   Input: nums = [7,2,4,6,5,8], target = 6
##   :: Output: min_length_subarr = 1, min_subarr = [6]
##
"""
##   Arrange the Steps
"""          
##           s
##   nums = [1,2,7,1,1,8], target = 9
##               e
##   1. Initialize the pointers for the sliding window,left and right, to both 
##      start at 0.
##   2. Initialize an empty array to hold the current valid subarray and 
##      a current sum variable to hold the current subarray sum.
##   3. Iterate the array, incrementing the right index until it reaches the end 
##      or length of the array.
##   4. In each iteration, check if the result of adding the value at the current 
##      index to the current subarray sum is equal to the target value. 
##       a. If the current subarray sum is equal to the target value, update the 
##          current valid subarray
##       b. If the current subarray sum is greater than the target value then 
##          the current window is invalid. Increment the start index by one, to 
##          make the the curent window subarray valid again.
##       c. If the current subarray sum is less than the target value, simply 
##          expand the current window by incrementing the end index and continue 
##          searching for a potential valid subarray.
##   5. If the length of the current valid subarray is less than the minimum 
##      subarray length, update the minimum subarray length as current valid 
##      subarray.
##   6. Return the minimum_subarray_length
##
"""
##   Write the Solution Code
def min_subarray_len(nums: str, target: int)->int:
    """   
    ##               s
    ##   nums = [1,2,7,1,1,8], target = 9
    ##                   e 
    ##          sum = 9 
    """
    start = 0
    output = []
    curr_subarray_sum = 0
    curr_subarray_length = 0
    min_subarray_length = float('inf')
    for index,value in enumerate(nums):
        curr_subarray_sum += value
        while curr_subarray_sum >= target:
            # current window subarray sum is greater than or equals to the 
            # target value,
            output = nums[start:index+1]
            curr_subarray_length = index-start+1
            min_subarray_length = min(curr_subarray_length, min_subarray_length)
            curr_subarray_sum -= nums[start]
            start += 1
    #return ([output,curr_subarray_sum],min_subarray_length if min_subarray_length != float('inf') else 0)
    return min_subarray_length if min_subarray_length != float('inf') else 0

##   Time Complexity
"""   
##    The time complexity of the solution is O(n), where n is the length of the 
##    input list nums. This is because we iterate through the list at most once 
##    using a for loop. The built-in Python functions used in the code such as 
##    min() and enumerate() have a time complexity of O(n) as well.
##
"""
##   Space Complexity
"""
##   The space complexity  of the solution is O(1) because it only uses 
##   a constant amoumt of extra space to store variables such as start, 
##   curr_sum, curr_length and min_length. The built-in Python functions invoked 
##   by the code such as enumerate, min, and float are not considered and do not 
##   factor or contribute to the space complexity as they do not use any 
##   additional space that grows with the input size.
##
"""
