# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Minimum Window Subsequence

##   Problem Statement
"""
##   Given two strings, str1 and str2, find the shortest substring in str1 
##   such that str2 is a subsequence of that substring.
##
##   SubString: A substring is defined as a contiguous sequence of characters within 
##   a string.

##   SubSequence: A subsequence is a sequence that can be derived from another 
##   sequence by deleting zero or more elements without changing the order of 
##   the remaining elements.
##
##   Example:
##   str1 = "abbcb", 
##   str2 = "ac"
##   In the above example, "abbc" is a substring of str1, from which we can 
##   derive str2 simply by deleting both instances of the character 
##   b. Therefore, str2 is a subsequence of this string. Since this substring 
##   is the shortest among all the substrings in which str2 is present as 
##   a subsequence, the function should return this substring, "abbc".
##
##   **Note**: If there is no substring in str1 that covers all characters in 
##   str2, return an empty string.
##   If there are multiple minimum-length substrings that meet the 
##   subsequence requirement, return the one with the left-most starting 
##   index.
##
##   Constraints:
##   * 1 <= str1.length <= 2 x 10^3
##   * 1 <= str2.length <= 100
##   * str1 and str2 consit of uppercase and lowercase English letterse
##
##   Example 1:
##   Input: str1 = "abcdebdde", str2 = "bde"
##   Output: "bcde"
##   Explanation: The strings "bcde" and "bdde" are both minimum subsequences, 
##                but "bcde" occurs before "bdde".
##                The substring "deb" is the shortest to contain all the 
##                required characters, but they do not appear in the required 
##                order.
##   Example 2:
##   Input: str1 = "abcdebdde", str2 = "bdf"
##   Output: ""
##   Explanation: str1 does not contain character "f" that's why an empty 
##                string is returned.
##
"""
##   Understand the Problem
"""
##   1. What are the valid substrings of "Educative"?
##   :: A) "tive", B) "cat"
##
##   2. In which string is "this" present as a subsequence?
##   :: A) "thims"
##
##   3. What is the output if the following strings are given as input?
##   Input: str1 = "this is a test string", str2 = "tis"
##   :: "this"
##
##   4. What is the output if the following strings are given as input?
##   Input: str1 = "asbfgedasfbdaaf", str2 = "bfd"
##   :: "bfged"
##
##   5. What is the output if the following strings are given as input?
##   Input: str1 = "Hello how are you?", str2 = "ok"
##   :: ""
##
"""
##   Arrange the Steps
"""
##   1. Begin iterating through str1 to locate a potential window that 
##      contains all the characters of str2 appearing in the required order.
##   2. Once you've identified a potential end, backtrack through the 
##      characters of str1 from this end position until you've found all the 
##      characters of str2 in reverse order.
##      This helps locate the potential start of the smallest subsequence.
##   3. Update the minimum window subsequence if the current window is smaller 
##      than the shortest subsequence found so far.
##   4. Repeat the process, starting every time from the second character of 
##      the current window, until the end of str1 has been reached.
##   5. Return the minimum window subsequence.
##
"""
##   Write the Solution Code
def min_window(str1,str2):
    n1,n2 = len(str1),len(str2)
    output = ""
    current_start = 0
    # locate potential end index
    e1,e2 = find_end(str1,str2,0,0,n1,n2)
    s1 = 0
    # if str2 pointer reached end, then subsequence has been found.
    if e2 == n2:
        # locate potential start index
        s1 = find_start(str1,str2,e1-1,n2-1,current_start)
        # set output to first window substr
        output = str1[s1:e1]
        min_substr_length = e1-s1 # 4-1=3
    current_start = s1
    while e1 < n1:
        e1,e2 = find_end(str1,str2,s1+1,0,n1,n2)
        # if str2 pointer reached end of str2, then look for potential start
        if e2 == n2:
            s1 = find_start(str1,str2,e1-1,n2-1,current_start)
            # update output if window size is smaller
            if (e1-s1) < min_substr_length:
                output = str1[s1:e1]
                min_substr_length = e1-s1
                current_start = s1
    return output
def find_end(str1,str2,e1,e2,n1,n2):
    """ str1: abcdefgbdhij, str2: bd 
    ##                ^
    ##  e1,e2 = 4,2
    ##  e1,e2 = 9,2
    ##  substr = abcd
    ##            ^
    ##  sustr = efgbd
    ##  str1 = abcdefgbd
    ##                ^
    ##  s1,s2 = 1,-1
    ##  s1,s2 = 7,-1
    ##  ** s1,e1 = 1,4
    ##  ** s1,e1 = 7,9
    ##  output = str1[s1:e1]
    """
    while e1 < n1 and e2 < n2:
        if str1[e1] == str2[e2]:
            e2 += 1
        e1 += 1
    return e1,e2
def find_start(str1,str2,s1,s2,start):
    while s1 >= start and s2 >= 0:
        if str1[s1] == str2[s2]:
            s2 -= 1
        s1 -= 1
    s1 += 1
    return s1

##   Solution Summary
"""
##   1. Initialize 2 indexes, p1 and p2, to zero for iterating the two strings 
##      str1 and str2.
##      Create two helper functions to locate potential start and end indexes 
##      for the sliding_window, which represents the current_substrings that 
##      are valid and satisfy the subsequence condition.
##   2. Locate the first potential substring's end index.
##   3. Iterate backward starting from the end index in the previous step to 
##      locate the first potential substring's start index.
##   4. Store the length of the first substring in a variable to track the 
##      minimum length of the substring that contains the required 
##      subsequence. Store the first substring found in an output variable.
##   5. Repeat steps 2-4, starting from the current_start+1 index until 
##      reaching the length (end) of str1 , and update the output variable 
##      accordingly as valid smaller length substrings that contain the 
##      required subsequence are found.
##   6. Finally, return the output.
##
##   AI Explanation:
##   1. The code starts by initializing variables and setting the initial 
##      values for the window.
##   2. It then finds the end index of the first occurrence of str2 in str1 
##      using the find_end function.
##   3. If str2 is found, it finds the start index of the window using the 
##      find_start function.
##   4. It updates the output and min_substr_length if the current window is 
##      shorter than the previous minimum.
##   5. The code continues to slide the window and update the output and 
##      min_substr_length if a shorter window is found.
##   6. Finally, it returns the output, which represents the minimum window 
##      that contains str2 as a subsequence.
##
"""
##   Time Complexity
"""
##   The time complexity of the function is O(n1 * n2), where n1 is the length 
##   of str1 and n2 is the length of str2. This is because the function iterates 
##   through str1 and str2 in nested loops, and the length of the output string 
##   can be at most n1. The find_end and find_start functions also have a time 
##   complexity of O(n1 * n2) in the worst case. The time complexity of built-in 
##   Python functions used in the code, such as string indexing and comparison, 
##   is O(1).
##
"""
##   Space Complexity
"""
##   The space complexity of the function is O(1) because it only uses a 
##   constant amount of extra space to store variables and does not use any 
##   additional data structures. The space complexity of the built-in Python 
##   functions invoked by the code is also O(1) because they do not use any 
##   additional space that grows with the input size.
##
"""
