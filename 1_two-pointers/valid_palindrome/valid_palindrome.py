# vim: set comments=sl\:\"\"\",m\:##\ \ \ \ ,ex-3\:\"\"\":
# vim: set fo=tcrq : 
# vim: set comments=sb\:\"\"\",mb\:##\ \ \ \ ,ex-3\:\"\"\",\:##:
# vim: set fo=tcq1rowabvpn:

##    Statement
"""
##    Write a function that takes a string, `s`, as an input and determines 
##    whether or not it is a palindrome.
##
##    **Note**: A palindrome is a word, phrase, or sequence of characters that 
##    reads the same backward as forward. For example: abcba
##
##    Constraints:
##    * 1 <= s.length <= 2 x 10^5
##    * The string `s` will not contain any white space and will only consist 
##    of ASCII characters.
##
##    Example 1:
##    Input: ABCBA
##    Output: True
##
##    Example 2:
##    Input: ABCCA
##    Output: False
##
"""
##    Understand the problem
"""
##    1. "abab" is a palindrome.
##    --> False
##    2. "RACEACAR" is a palindrome.
##    --> False
##    3. "RACECAR' is a palindrome.
##    --> True
##    4. Suppose you could swap just two characters in the following string to 
##       make a palindrome.
##       s = "abab"
##       Which combination could we come up with?
##       --> "baab"
"""
##    Arrange the Steps
"""
##    1. Initialize the pointers at the beginning and end of the string
##    2. Check whether or not the current pair of characters is identical.
##    3. If they are not identical, return FALSE. Otherwise, move both 
##       pointers by one index toward the middle.
##    4. Keep traversing them toward the middle until they meet.
##    5. If we reach the middle of the string without finding a mismatch, 
##       return TRUE.
"""
##    Write the Solution Code
def ispalindrome(s:str)->bool:
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

##    Solution Summary
"""
##    - Initialize two pointers and move them from opposite ends.
##    - The first pointer starts at the beginning of the string and moves
##    toward the midle, while the second pointer starts at the end and moves
##    toward the middle.
##    - Compare the elements at each position to detect a nonmatching pair.
##    - If both pointers reach the middle of the string without encountering
##    a nonmatching pair, the string is a palindrome.
##    
"""
##    Time Complexity
"""
##    The time complexity is O(n), where n is the number of characters in the
##    string. However our algorithm only runs (n/2) times, since two pointers
##    are traversing toward each other.
##
"""
##    Space Complexity
"""
##    The space complexity is O(1), since we use constant space to store two 
##    indexes.
