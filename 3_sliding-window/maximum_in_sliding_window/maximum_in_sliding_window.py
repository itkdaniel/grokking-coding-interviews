# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

## Find Maximum in Sliding Window
##
##    Problem Statement
"""
##   Given an integer list, nums, find the maximum values in all the 
##   contiguous subarrays (windows) of size w.
##
##   **Note**: If the window size is greater than the array size, we consider 
##   the entire array as a single window.
##
##   Constraints:
##   * 1 <= arr.length <= 10^3
##   * -10^4 <= arr[i] <= 10^4
##   * 1 <= w
##
##   Example 1:
##   Input: nums = [-4,2,-5,3,6], w = 3
##   Output: [2,3,6]
##
##   Example 2:
##   Input: nums = [1,2,3,4,5,6], w = 6
##   Output: [6]
##
##   Example 3:
##   Input: nums = [1,2,3,4,5,6,7,8,9,10], w = 4
##   Output: [4,5,6,7,8,10]
##
"""
##   Arrange the Steps
"""
##   1. Initialize an empty deque data structure.
##   2. Iterate through the first w elements in the input array, performing 
##      cleanup operations on the deque to maintain a decreasing order of 
##      values.
##   3. Store the maximum value of the initial window.
##   4. Slide the window through the array, updating the deque and storing 
##      maximum values for each window.
##
"""
##   Write the Solution Code
from collections import deque   

def maintenence_cleaning(i, window, nums):
    while window and nums[i] >= nums[window[-1]]:
        window.pop()

def find_max_sliding_window(nums:list[int],w:int)->list:
    left,right = 0,0+w
    output,window = [],deque()
    n = len(nums)
    if n == 0:
        return []
    if w > n:
        w = n
    for i in range(w):
#        while window and nums[i] >= nums[window[-1]]:
#            window.pop()
        maintenence_cleaning(i,window,nums)
        window.append(i)
    output.append(nums[window[0]])
    for i in range(w,n):
#        while window and nums[i] >= nums[window[-1]]:
#            window.pop()
        maintenence_cleaning(i,window,nums)
        if window and window[0] <= (i-w):
            window.popleft()
        window.append(i)
        output.append(nums[window[0]])
    return output

##   Solution Summary
"""
##   First, instead of adding values to the sliding_window, we use their 
##   indexes.
##      - This makes it easy to check which index has fallen out of the 
##        current window and remove it.
##   Second, we process the elements of the first window as follows:
##      - Every time we add a new index to the sliding_window, we pop() and 
##        remove the every last entry (index) in the window whose corresponding 
##        values in the input list are smaller or equal to the new element 
##        being added to the window.
##      - Explanation: This benefits us because:
##          - Whenever a new element enters the window, all previous elements 
##            smaller than the current element being added can no longer be 
##            the maximum in the current or subsequent windows containing the 
##            new element.
##            This is because all the subsequent windows holding the indexes 
##            of the removed elements will also include the new, bigger 
##            element. Since the new element is bigger than those elements, 
##            keeping the smaller elements in the window is unnecessary.
##      - A key detail to note here is that we perform the validity check 
##        (pop() and remove last indexes) step starting with the **second** 
##        element added to the first window. 
##        As a result, even in the first window, we will have excluded all 
##        elements smaller than the maximum of that window that occurs before 
##        it in the input list.
##      - For example: [2,4,5,3,1] - When the index of value 4 is added to the 
##        window, it causes the index 2 to be removed. The addition of the 
##        index of value 5 causes the index of value 4 to be removed. However, 
##        the addition of the indexes of values 3 and 1 do not trigger any 
##        removals because they are NOT bigger than the value of the window's
##        last index's element in the input list.
##        At the end of this clean-up process, the current_window contains the 
##        indexes, [2,3,4], corresponding to the values, [5,3,1].
##      - Once the first window has been checked and cleaned to be valid, the 
##        remaining indexes in the current_window will be stored in descending 
##        order of their values. 
##        ** Another possibility, is where the first frame actually contains 
##        [2,4,5,1,3]. Here, the addition of the index 1 does not trigger any 
##        removals (deletion), but 3 does cause the index 1 to be removed 
##        (deleted). Then, current_window now holds the indexes [2,4], 
##        corresponding to values [5,3] in the input list, which are sorted in 
##        descending order. 
##        Since we've examined both possibilities:
##          1. Elements in nums after element 5 are in descending order
##          2. "                              " are NOT in descending order
##        we can be sure that, after the clean-up process, the index of the 
##        maximum element in the first window will always be stored at the 
##        start of the current_window.
##      - We append the value corresponding to the index at the start of the 
##        current_window to the output list.
##   Next, we iterate over the remaining input list. For each element, we 
##   perform the clean-up step as we did for the elements in the first window.
##   The difference in processing the second and all subsequent windows, 
##   compared to the processing of the first window, is an additional check 
##   that is carried out BEFORE we append the current element in nums to the 
##   current_window. We check whether the first index in the current_window is 
##   still a part of the current_window. If not, we remove the FIRST index 
##   from the current_window.
##
##   Lastly, when the entire input list has been processed, one window at 
##   a time, we return the output list containing the maximum values of each 
##   window.
##
"""
##   Solution Steps
"""
##   1. First, we validate the inputs. If the input list is empty, we return 
##      an empty list and if the window size is greater than the length of the 
##      input list, we set the window to be the same size as the input list.
##   2. Then, we process the first w elements of the input list. We use 
##      a deque() to store the indexes of the candidate maximums of each 
##      sliding_window iteration.
##   3. For each element, we perform the maintenence clean-up step, removing 
##      the indexes of the elements from the end of the deque() whose values 
##      are smaller than or equal to the value currently being added to the 
##      deque(). Then, we append the index of the new element to the end of 
##      the deque().
##   4. After the first w elements have been processed, we append the element 
##      whose index is present at the front of the deque() to the output list 
##      since it is the maximum of the first window.
##   5. After finding the maximum in the first window, we continue iterating 
##      over the remaining input list. 
##      For each element, we repeat Step 3, as we did for the first 
##      w elements.
##   6. Additionally, in each iteration, before appending the index of the 
##      current element to the deque(), we check if the first index in the 
##      deque() is still within the bounds of the window size. If not, we 
##      remove it from the deqeue().
##   7. Finally, we return the list containing the maximum elements of each 
##      window.
##
"""
##   Time Complexity
"""
##   Using the sliding window, we are iterating over the input list in O(n) 
##   time while maintaining the window. Inside the loop we append the new 
##   element to current_window, which takes O(1) time. The time complexity of 
##   the clean-up step is O(1). Then, we remove the index that is outside of 
##   the current_window from the start (front) of the list, which takes 
##   O(w). Therefore, the overall time complexity of this solution will be 
##   O(n*w).
##
"""
##   Space Complexity
"""
##   The space complexity of this solution is O(w), because we maintain a list 
##   to store the indexes of significant elements from the current_window.
##
"""
