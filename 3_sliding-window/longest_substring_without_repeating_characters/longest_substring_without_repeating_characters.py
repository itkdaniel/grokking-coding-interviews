# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Longest Substring Without Repeating Characters
##
##   Problem Statement
"""
##   Given a string, input_str, return the length of the longest substring 
##   without repeating characters.
##
##   Constraints:
##   * 1 <= input_str.length <= 5 x 10^4
##   * input_str consists of English letters, digits, symbols, and spaces.
##
##   Example 1:
##   Input: string = "bbbbbb"
##   Output: 1
##
##   Example 2:
##   Input: string = "pwwkew"
##   Output: 3
##
##   Example 3:
##   Input: string = ""
##   Output: 0
##
"""
##   Understand the Problem
"""
##   1. What should be the output if the following string is given as an input?
##   Input: str = "conceptoftheday"
##   :: Output: oftheday -> 8
##
##   2. What should be the output if the following string is given as an input?
##   Input: str = "bbbbbbbbbbbbbbbb"
##   :: Output: b -> 1
##
##   3. What should be the output if the following string is given as an input?
##   Input: str = "racecar"
##   :: Output: race -> 4
##
##   4. What should be the output if the following string is given as an input?
##   Input: str = "bankrupted"
##   :: Output: bankrupted -> 10
##
"""
##   Arrange the Steps
"""
##   1a. Initialize a hashmap/dictionary to store the frequency of each character 
##       in the current window along with the last index where it was seen.
##   1b. Initialize an empty hash map and a variable to track character indexes 
##       and the start of the window respectively.
##   2a. Initialize and maintain 2 variables, left and right, both starting from 
##       index 0, representing the start and end of the sliding window.
##   2b. Traverse the string character by character. For each character, if the 
##       hash map does not contain the current character, store it with its 
##       index as the value.
##   3a. Begin iterating the string by moving the right pointer by 1.
##   3b. If the hash map contains the current character and its index falls 
##       within the current_window, a repeating character is found. Otherwise, 
##       store it in the hash map with its index as the value.
##   4a. If the character has not been seen yet, then add it to the hashmap along 
##       with its index and increment the right pointer.
##   4b. When a repeating character is found, update the previous location of 
##       the current element and increment it. Also, calculate the length of the 
##       cureent window.
##   5a. Maintain an output variable that holds the length of the longest 
##       substring without repeating characters.
##   5b. Update the longest substring seen so far if the length of te current 
##       window is greater than its current value.
##   6a. If the string in the current window is valid and its length is greater 
##       than the longest_substring_without_repeating_chars variable, then update 
##       the longest_substring variable with the length of the current window 
##       (right-left+1).
##   6b. Return the length of the longest substring.
##   7a. If the character already exists in the hashmap, the window has become 
##       invalid due to encounter of duplicate character. Make the window valid 
##       again by moving the left pointer to the index it was last seen at plus 
##       1. Recalculate and update the size of the current_window accordingly 
##          (i.e if the length of the current_window is greater than current 
##          value; value is length of the longest_substring variable).
##   8a. Repeat steps 4-7 until reaching the end of the string.
##   9a. Return the longest substring without repeating characters.
##
"""
##   Write the Solution Code (Self Algorithm)
from collections import defaultdict
def find_longest_substring(input_str: str)->int:
    """
    ##    abc    d
    ##   "conceptoftheday"
    ##    012345678901234
    ##      a   b c     d
    ##   max_substr_length = max(x2-x1+1,max_substr_length)
    ##
    """
    start = 0
    output = longest_substr = 0
    current_length = 0
    current_window = {}
    for index,char in enumerate(input_str):
        # current character is already present in the current_window
        if char in current_window:
            # if the last index of the current character is
            # within the current substring
            if current_window[char] >= start:
                # update the start index of the current substring to be:
                # one after the last index the current character was seen
                start = current_window[char] + 1
        # update hashmap value to the index of the current character 
        current_window[char] = index
        # update the current substring length as: index-start+1
        current_length = index-start+1
        # update the length of the longest valid substring (substring without 
        # repeating characters/output/return value) if the new/current substring 
        # length is greater than the current longest valid substring.
        output = max(current_length,output)
    return output
def find_longest_substring2(input_str: str)->int:
    start = 0
    output = 0
    max_substr_length = 0
    char_map: defaultdict[str,int] = defaultdict(int)
    for index,char in enumerate(input_str):
        if char not in char_map:
            char_map[char] = index
        else:
            if char_map[char] >= start:
                start = char_map[char]+1
            char_map[char] = index
        max_substr_length = index-start+1
        output = max_substr_length if max_substr_length > output else output
    return output
def find_longest_substring3(input_str: str)->int:
    """   
    ##     s                  
    ##    "conceptoftheday"
    ##     e                  
    ##    char_map = {
    ##      ...
    ##    }
    ##    left,right = 0,0
    ##    max_substr = ""
    ##    max_substr_length = 0
    ##
    """
    output = 0
    start = 0
    max_substr_length = 0
    char_map: defaultdict[str,int] = defaultdict(int)
    for index,char in enumerate(input_str):
        if char not in char_map:
            char_map[char] = index
        else:
            temp = char_map[char]+1
            for i in range(start,temp):
                del char_map[input_str[i]]
            start = temp
            char_map[char] = index
        max_substr_length = index-start+1
        if max_substr_length > output:
            output = max_substr_length
    return output

##   Time Complexity
"""
##   The time complexity of this solution is O(n), where n is the length of the 
##   input string. This is because we iterate through the input string at most 
##   once, and for each character, we perform constant time operations such as 
##   checking if it is in the current window hashmap, adding or removing 
##   elements from the hashmap, and updating the start and max_length 
##   variables. The time complexity of built-in Python functions such as del and 
##   enumerate are also O(1) and do not affect the overall time 
##   complexity. Therefore the final time complexity is O(n).
##
"""
##   Space Complexity
"""
##   The space complexity of the function to find the longest substring without 
##   repeating characters is O(n), where n is the length of the input 
##   string. This is because we are using a hashmap, char_map, to store the 
##   characters and their indicies for the current window. The size of the 
##   hashmap can grow up to the length of the input string in the worst case 
##   scenario where there are no repeating characters. Additionally, we are 
##   using a few variables (start, max_length) to keep track of the current 
##   window and the maximum length of the valid substring, which requires 
##   constant space. The space complexity of the built-in Python functions 
##   invoked by the code is not considered in this analysis.
##
"""
