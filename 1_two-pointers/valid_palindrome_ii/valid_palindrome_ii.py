# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

##   Problem Statement
"""
##   Write a function that takes a string as input and checks whether it can 
##   be a valid palindrome by removing at most one character from it.
##
##   Constraints:
##   * 1 <= string.length <= 10^5
##   * The string only consists of English letters
##
##   Example 1:
##   Input: "ABCEBA"
##              ^
##   Output: True
##
##   Example 2:
##   Input: "RACEACAT"
##   Output: False
##
##   Example 3:
##   Input: "DEEAD
##              ^
##   Output: True
##
"""
##   Understand the Problem
"""
##   1. Can "RACEACAR" be a palindrome?
##               ^
##   :: --> Yes
##
##   2. Can "abbababa" be a palindrome?
##            ^^
##   :: --> Yes
##
##   3. Can "abcedca" be a palindrome?
##   :: --> No
##
"""
##   Arrange the Steps
"""
##   1. Initialize two pointers at opposite ends of the string.
##   2. If the vales at the left and right indexes match, move both toward the 
##      middle until they meet.
##   3. If a mismatch occurs, skip one of the elements and check the rest of 
##      the string for a palindrome.
##   4. Skip the other element, and check for the palindrome.
##   5. If no palindrome is obtained, return False, else if no more than one 
##      mismatch occurs throughout the traversal, return True.
##
"""
##   Write the Solution Code
"""
##   **Hint**: The optimal solution to this problem runs in O(n) and takes 
##   O(1) space.
##
"""
##   Approach 1
"""          1 2
##   a b b a b a b a
##       1 2       
##             v
##   m a d a m e
##   ^
"""
def is_palindrome(s:str)->bool:
    def _is_palindrome(s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    n = len(s)
    left,right = 0,n-1
    while left < right:
        if s[left] != s[right]:
            tleft1,tright1 = left,right-1
            tleft2,tright2 = left+1,right
            if (not _is_palindrome(s,tleft1,tright1) and not 
                    _is_palindrome(s,tleft2,tright2)):
                return False
        left += 1
        right -= 1
    return True
