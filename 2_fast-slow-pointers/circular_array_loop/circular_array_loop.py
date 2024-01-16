# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Problem Statement
"""
##   An input array, nums containing non-zero integers, is given, where the 
##   value at each index represents the number of places to skip forward (if 
##   the value is positive) or backward (if the value is negative). When 
##   skipping forward or backward, wraap around if you reach either end of the 
##   array. For this reason, we are calling it a cirular array. Determine if 
##   this ciruclar array has a cycle. A cycle is a sequence of indicies in the 
##   cirular array characterized by the following:
##
##   * The same set of indicies is repeated when the sequence is traversed in 
##   accordance with the aforementioned rules.
##   * The length of the sequence is at least two
##   * The loop must be in a single direction, forward or backward.
##
##   It should be noted that a cycle in the array does not have to originate 
##   at the beginning. A cycle can begin from any point in the array.
##
##   Constraints:
##   * i <= nums.length <= 10^4
##   * -5000 <= nums[i] <= 5000
##   * nums[i] != 0
##
##   Example 1:
##   Input: [3,1,2]
##   Output: True
##   Explanation:
##    f
##   [3, 2, 1]
##    s
##      Case 1:
##          1. Set starting point slow,fast=0,num_in_seq=1,dir=0,cur=0
##          2. for i in arr
##          3. set slow=fast=i
##              - if a[fast] < 0 -> set start=pos
##              - else -> set start=neg
##              while fast != slow and dirch==0;
##                  - ?? free_conditional...
##                      - if a[fast] > 0
##                          - if start!=pos
##                              -> do dirch+=1
##                          -> if fast+a[fast] > n-1
##                              -> do fast=(fast+a[fast])%n
##                          -> else
##                              -> fast=fast+a[fast]
##                      - else;
##                          - if start!=neg
##                              -> do dirch+=1
##                          -> if fast-a[fast] < 0
##                              -> do fast=(fast+a[fast])%n
##                          fast-=a[fast]
##                              - if fast-a[fast] < 0
##                                  -> do fast=n-((fast+abs(a[fast]))%(n-1))
##                  - incr num_in_seq+1
##              4. if num_in_seq > 1 and dirch==0
##                  - cycle detected ✓
##                  - return True
##          5. return False
##   
##   Example 2:
##   Input: [-2, -1, -3]
##   Output: True
##      - Flow:
##          slow = 0
##          fast = a[slow] if a[slow] < n-1 else a[slow]%n
##          start = (slow,fast)
##          while slow neq fast
##              -> if slow == n and nseq == 0
##                  - invalid cycle
##                  - break
##              -> if fast+a[fast] > n-1
##                  - if fast == a[fast+a[fast]%n]
##                      - invalid cycle
##                      - break
##              -> else
##                  - if fast == a[a[fast]]
##                      - invalid cycle
##                      - break
##              -> if fast == slow
##                  return true
##   
##   Example 3:
##   Input: [2,1,-1,-2]
##   Output: False
"""
##   Arrange the Steps
"""
##   1. Traverse the entire nums array moving slow and fast pointers, starting 
##      from index 0.
##   2. Move the slow pointer one time forward/backward and the fast pointer 
##      two times forward/backward
##   3. If loop direction changes at any point or taking a step returns to the 
##      same location, continue to the next element.
##   4. If direction does not change, check whether both pointers meet at the 
##      same node, if yes, then loop is detected, return True.
##   5. Return False if don't encounter a loop after traversing the whole 
##      array.
##
"""
def circular_array_loop(nums:list[int])->bool:
    n = len(nums)
    for i,e in enumerate(nums):
        pos = 1 if e > 0 else 0
        chdir = 0
        seq_length = 0
        slow,fast = i,nums[i]
        temp = -slow
        print(f'checking cycle for i={i}')
        while fast != slow:
            temp = slow
            prev = fast
            if nums[slow] > 0:
                # check if start was positive
                if not pos or (abs(nums[slow]) == n and seq_length < 1):
                    # if start was not positive,continue next element
                    break
                #if slow+nums[slow] < n-1:
                #    slow = slow+nums[slow]
                #else:
                #    slow = (slow+nums[slow])%n
                seq_length += 1
                if slow+nums[slow] < n-1:
                    fast = slow+(nums[slow])
                else:
                    fast = (slow+(nums[slow]))%n
                if nums[fast] < 0 or nums[(fast+nums[fast])%n] < 0:
                    # invalid cycle, dirch
                    chdir += 1
                    break
            else:
                if pos or (abs(nums[slow]) == n and seq_length < 1):
                    # if start was not negative,continue next element
                    break
                #if slow-abs(nums[slow]) > 0:
                #    slow = slow-abs(nums[slow])
                #else:
                #    slow = n-(slow+abs(nums[slow]))%(n-1)
                seq_length += 1
                if (fast+nums[fast])%n > 0:
                    #fast = slow-nums[slow]-nums[nums[slow]]
                    fast = (fast+nums[fast])%n
                else:
                    #fast = n-(slow+abs(nums[slow])+abs(nums[abs(nums[slow])]))%(n-1)
                    fast = (fast+nums[fast])%n+n
                if nums[fast] > 0:
                    # invalid cycle
                    chdir += 1
                    break
            print(f'{slow=}, {fast=}, {seq_length=}')
            if (fast == slow or fast == temp or fast == prev) and not chdir and seq_length > 0:
                return True
    return False

##  Educative.io Solution.
def circular_array_loop(nums:list[int])->bool:
    n = len(nums)
    for i,e in enumerate(nums):
        slow = fast = i
        chdir = nums[slow] > 0
        while True:
            slow = (slow + nums[slow]) % n
            slow = slow if slow < 0 else slow + (n-1)
            cwdir = nums[slow] >= 0
            if (chdir != cwdir) or (abs(nums[slow]%(n-1) == 0)):
                break
            for i in range(2):
                fast = (fast + nums[fast]) % n
                fast = fast if fast < 0 else fast + (n-1)
                cwdir = nums[fast] >= 0
                if (chdir != cwdir) or (abs(nums[fast]%n == 0)):
                    break
            if slow == fast:
                return True
    return False

