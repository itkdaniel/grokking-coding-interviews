# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Problem Statement
"""
##   Given an unsorted array of positive numbers, nums, such that the values 
##   lie in the range [1,n], inclusive, and that there are n+1 numbers in the 
##   array, find and return the duplicate number present in nums. There is 
##   only one repeated number in nums.
##
##   **Note**: You cannot modify the given array nums. You have to solve the 
##   problem using only constant space.
##
##   Constraints:
##   * 1 <= n <= 10^5
##   * nums.length = n+1
##   * 1 <= nums[i] <= n
##   * All integers in nums are unique, except for the one integer that will 
##   appear more than once.
##
##   Example 1:
##   Input: [1,3,3,4,2,5]
##   Output: 3
##
##   Example 2:
##   Input: [1,5,3,4,2,5]
##   Output: 5
##
##   Example 3:
##   Input: [1,2,3,4,5,6,6,7]
##   Output: 6
##
##   Example 4:
##   Input: [4,6,7,7,3,5,2,8,1]
##   Output: 7
##
##   Example 5:
##   Input: [9,8,7,6,2,3,5,4,1,9]
##   Output: 9
##
"""
##   Arrange the Steps
"""
##   1. Traverse nums using two pointers slow and fast initially set to start 
##      of the array.
##   2. Move the pointers until they meet. The slow pointer moves once while 
##      the fast pointer moves twice as fast as the slow pointer (i.e twice).
##   3. After the pointers meet, traverse the nums array once again.
##   4. Move the slow pointer from the start of nums and the fast pointer from 
##      the meeting point (where it left off) at the same speed (one step) 
##      until they meet again.
##   5. Return the fast pointer.
##
"""
##   Write the Solution Code
def find_duplicate_number(nums:list[int])->int:
    n = len(nums)
    slow,fast = 0,0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    if slow == fast or nums[slow] == nums[fast]:            
        print(f'duplicate is {nums[fast]=}')
        return fast
    return False

##   Time Complexity
"""
##   the time complexity of this algorithm is O(n), where n is the length of 
##   nums. Since, in each part of the solution, the slow pointer traverses 
##   the nums array at most one time.
##
"""
##   Space Complexity
"""
##   The algorithm takes O(1) space complexity, since only a constant amount 
##   of space was used to store fast and slow pointers.
##
"""
