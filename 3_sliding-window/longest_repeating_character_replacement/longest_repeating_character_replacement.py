# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##,\:#:
# vim: set fo=tcq1rowpn:

##   Longest Repeating Character Replacement
##
##   Problem Statement
"""
##   Given a string, s, of lowercase English characters and an integer, k, 
##   return the length of the longest substring after replacing at most 
##   k characters with any other lowercase English character so that all the 
##   characters in the substring are the same.
##
##   Constraints:
##   * 1 <= s.length <= 10^5
##   * s consist of only lowercase English characters
##   * 0 <= k <= s.length
##
##   Example 1:
##   Input: s = "aabccbb", k = 2
##   Output: length_of_longest_substr = 5
##   Explanation: All the characters of the substring "bccbb" can be the same 
##   if we replace all the instances of "c" with "b". The length of this 
##   substring is 5, and it is the longest substring, which will consist of 
##   the same after, at most k replacements.
##
##   Example 2:
##   Input: s = "fzfzfz", k = 6
##   Output: length_longest_substr = 6
##   Explanation: All the characters of the substring "fzfzfz" can be the same 
##   if we replace all instances of "z" with "f". The length of this substring 
##   is 6, and it is the longest substring, which will consist of the same 
##   character after, at most, k replacements. We can achieve the same thing 
##   by replacing all instances of "f" with "z".
##
"""
##   Understand the Problem
"""
##   1. What is the correct output for the following input values?
##   Input: s = "abab", k = 2
##   :: length_of_longest_substr = 4
##
##   2. What is the correct output for the following input values?
##   Input: s = "dippitydip", k = 4
##   :: length_of_longest_substr = 6
##
##   3. What is the correct output for the following input values?
##   Input: s = "roller", k = 2
##   :: length_of_longest_substr = 4
##
"""
##   Arrange the Steps
"""
##   1. Iterate over the input string using the sliding window pattern. Do 
##      this while maintaining a variable to store the length of the longest 
##      substring with the same characters after replacement.
##   2. Maintain a hash map to store the frequency of all the characters in 
##      the current window.
##   3. If the number of replacements in the current window have exceeded our 
##      limit, slide the window one step forward.
##   4. If the current window is the longest so far, store the length of this 
##      window.
##   5. Return the length of the longest substring.
##
"""
##   Educative Solution
def longest_repeating_character_replacements2(s:str,k:int)->int:
    n = len(s)
    start,end = [0]*2
    output = 0
    max_substr_len = 0
    current_window = {}
    most_freq_char_count = 0
    most_freq_char = s[0]
    num_replacements = 0
    while end < n:
        if s[end] not in current_window:
            current_window[s[end]] = 1
        else:
            current_window[s[end]] += 1
        # if current char frequency > most_freq_char
        # update most_freq_char to frequency of current char
        if current_window[s[end]] > most_freq_char_count:
            most_freq_char_count = current_window[s[end]]
            most_freq_char = s[end]
            num_replacements = end-start+1-most_freq_char_count
        if s[end] != most_freq_char:
            num_replacements += 1
        # check if window is still valid:
        # if num_replacements > k, window is invalid.
        # (i.e current max substr length is invalid 
        # make the window valid again by:
        # 1. subtract the frequency of the character at the start of the window 
        #    by 1, and
        # 2. make the window valid again by sliding the window forward one step,
        #    (i.e increment start index by 1).
        if num_replacements > k:    
#        if start-end+1-current_window[most_freq_char] > k:
            current_window[s[start]] -= 1
            start += 1
            num_replacements -= 1
        # check if most_freq_char should be updated
        if s[start] == most_freq_char:
            if current_window[s[end]] > current_window[most_freq_char]:
                most_freq_char_count = current_window[s[end]]
                most_freq_char = s[end]
            else:
                most_freq_char_count = current_window[most_freq_char]
        if end-start+1 > output:
            output = end-start+1
        end += 1
    return output
    
##   Self Write the Solution Code
def longest_repeating_character_replacements(s:str, k:int)->int:
    """
    ##   s = "aaacbbbaabab", k = 2
    ##   s = "dippitydip", k = 4
    ##            s     e               
    ##             e  e
    ##   s,e = 4,10
    ##   cwindow = {d:1,i:2,p:1,t:1,y:1}
    ##   mfc,mfcc = i,2
    ##   r = 4
    ##   out = 6
    """
    n = len(s)
    start,end = 0,-1
    num_replacements = 0
    output = float('-inf') 
    longest_repeated_char = float('-inf')
    current_window = {}
    current_longest_char = s[0]
    while end < n-1:
        end += 1
        if s[end] in current_window:
            # same character, incr its count
            if s[end] == current_longest_char:
                current_window[current_longest_char] += 1
            else:
                # different character, check if can make replacement
                if num_replacements < k:
                    num_replacements += 1
                    current_window[current_longest_char] += 1
                else:
                    # maxed out replacements, slide the window
                    current_window = {}
                    start += 1
                    end = start-1
                    num_replacements = 0
                    current_longest_char = s[start]
        else: 
            # not in current window
            if s[end] == current_longest_char:
                current_window[s[end]] = 1
            else:
                current_window[s[end]] = 1
                # try to replace
                if num_replacements < k:
                    num_replacements += 1
                    current_window[current_longest_char] += 1
                else:
                    # slide the window
                    current_window = {}
                    start += 1
                    end = start-1
                    num_replacements = 0
                    current_longest_char = s[start]
        if current_longest_char in current_window:
            current_longest_char = s[end] if current_window[s[end]] > current_window[current_longest_char] else current_longest_char
            if current_window[current_longest_char] > output: 
#                output = current_window[current_longest_char]
                output = max(current_window[current_longest_char],current_window[s[end]])
    return output

##   Solution Walk-Thru
"""
##   Review by Educative.io AI:
##   Yes, the Sliding Window pattern is used in the code. The code maintains 
##   a window of characters and slides it to process sequential data.
##   The code follows proper language guidelines. It uses meaningful variable 
##   names, has proper indentation, and includes comments to explain the 
##   logic.
##
##   Review:
##      ✓ The code correctly initializes the necessary variables
##      ✓ It iterates through the string using a sliding window approach
##      ✓ It handles cases where the current character is already in the 
##        window or not.
##      ✓ It checks if a replacement can be made or if the window needs to 
##        slide.
##      ✓ It updates the output variable with the length of the longest 
##        repeated character.
##      ✓ The code returns the correct output.
##   
##   Overall, the code appears to be correct and follows the Sliding Window 
##   pattern to solve the problem. ✓✓✓
##
"""
##   Time Complexity
"""
##   The time complexity of this solution is O(n), where n is the length of 
##   the input string. ✓
##   This is because the function iterates through the input string at most 
##   once using te sliding window approach. The time complexity of the 
##   built-in Python functions used in the code, such as dictionary operations 
##   and string comparisons, are typically O(1) i.e constant time.
##
"""
##   Space Complexity
"""
##   The space complexity of this solution is O(1).
##   This is because the space used by the function does not depend on the 
##   size of the input string. The function only uses a constant amount of 
##   space to store variables such as start, end, num_replacements, output, 
##   current_window, and current_longest_char. The space complexity of the 
##   built-in Python functions invoked by the code is also O(1) as they do not 
##   use any additional space proportional to the input 
##   size. \x1b[1;32m✓✓✓\x1b[0m
##
"""
