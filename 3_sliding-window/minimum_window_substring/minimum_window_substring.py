# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Minimum Window Substring
##
##   Problem Statement
"""
##   Given two strings, s and t, find the minimum window substring in s, which 
##   has the following properties:
##    1. It is the shortest substring of s that includes all of the characters 
##       present in t.
##    2. It must contain at least the same frequency of each character as in 
##       t.
##    3. The order of the characters does not matter here.
##
##    **Note**: If there are multiple valid minimum window substrings, return 
##              any of them.
##
##    Constraints:
##    * Strings s and t consist of uppercase and lowercase English characters.
##    * 1 <= s.length,t.length <= 10^3
##
##    Example 1:
##    Input: s = "ABAACBBA", t = "ABC"
##                   s e
##    {a:1,b:1,c:1},{a:1,b;1,c:1},fm=3
##    Output: "ACB":: "BAAC"
##    
##    Example 2:     s
##    Input: s = "ACBBACA", t = "ABA"
##                      e   
##    {A:2,B:1}, {A:2,B:1}, fm=2, o=BACA
##    Output: "BACA"
##
##    Example 3:
##    Input: s = "ABAACBAB", t = "ABCC"
##    Output: "" (Thre are no substrings of t in s that: 
##                  1. have all characters of t, and 
##                  2. contains at least the same frequency of each character of t)
##                  
"""
##   Understand the Problem
"""
##   1. What is the output if the following strings are given as input?
##   Input: s = "cabwefgewcwaefgcf", t = "cae"
##   :: "cwae"
##
##   2. What is the output if the following strings are given as input?
##               s»·,trail:·,nbsp:·
##   Input: s = "bbaac", t = "aba"
##                  e
##   {a:2,b:1},{b:2,a:2},fm=3
##   :: "baa"
##
##   3. What is the output if the following strings are given as input?
##   Input: s = "AbabbbAbaA", t = "Bab"
##   :: ""
##
"""
##   Arrange the Algorithm Steps
"""
##   "cabwefgewcwaefgcf", "cae"
##            s    e
##                    e
##               s
##   {c:1,a:1,e:1}
##   {e:1,c:1,a:1}
##   start,end = (0,4), (7,11), (9,12), (11,15)
##   min_substr = "cabwe"
##   min_substr_len = start-end+1 = 4
##
##   1. Iterate the string t and create a hash map of each character's 
##      frequency for string t.
##   2. Iterate the string s while maintaining the count of each character of 
##      t found in s for the current window using a second hash map.
##   3. Each time a character from t is found in s, get the difference of the 
##      characters frequency from each string. 
##   4. If the difference of the character count is 0, then the window is 
##      valid.
##   5. If the difference is positive, then the window contains too many of 
##      that character. Slide the window forward until reaching another 
##      character that is from string t.
##   6. If the difference is negative, the window does not have enough of that 
##      character, add 1 to the characters count in hash map of s, and 
##      continue expanding the window.
##   
"""
##   Arrange the Algorithm Steps - Educative Solution
"""
##   1. Set up sliding window to move acrosss te string s.
##   2. Initialize 2 collections:
##      - 1 to get the frequency of the characters in string t
##      - 2 to track the frequency of characters from string s for the current 
##        window.
##   3. Iterate over s, expanding the current window until the frequencies of 
##      characters of t in the window are at least equal to their respective 
##      frequencies in s.
##   4. Trim/adjust/validate the window by removing all unneccessary 
##      characters. If the current_window size is less than the length of the 
##      minimum window substring found so far, update the minimum window 
##      substring.
##   5. Continue iterating over s and repeat steps 3-4 until reaching the end 
##      of the string.
##   6. Return the minimum window substring.
##
"""
##   Write the Solution Code
from collections import Counter  
def minimum_window_substring(s:str,t:str)->str:
    """
    ##                  s
    ##   s "cabcwefgewcwaefgcf", t = "cae"
    ##                       e
    ##      left,right = 10,13
    ##      t-map = {c:1,a:1,e:1}
    ##      s-map = {c:1,a:1,e:1}
    ##      min-substr-len = 4
    ##      min-subtr = s[10:14] = "cwae"
    """
    n = len(s)
    left,right = [0]*2
    output = ""
    t_char_freq = Counter(t)
    s_char_freq = {}
    freq_matches = 0
    while right < n:
        if s[right] in t_char_freq:
            if s[right] not in s_char_freq:
                s_char_freq[s[right]] = 1
            else:
                s_char_freq[s[right]] += 1
            if s_char_freq[s[right]] - t_char_freq[s[right]] == 0:
                freq_matches += 1
        if freq_matches == len(t_char_freq):
            # revalidate the window by moving the start index to the next
            # occurrence of a character that is also in string t.
            while s[left] not in t or s_char_freq[s[left]] - t_char_freq[s[left]] > 0:
                if s[left] in t:
                    s_char_freq[s[left]] -= 1
                    if s_char_freq[s[left]] < t_char_freq[s[left]]:
                        freq_matches -= 1
                    left += 1
                else:
                    left += 1
        if len(s_char_freq) == len(t_char_freq) and freq_matches >= len(t_char_freq) and sum(s_char_freq.values()) >= sum(t_char_freq.values()):
            if not output:
                output = s[left:right+1]
            else:
                if right-left+1 < len(output):
                    output = s[left:right+1]
        right += 1
    return output

def minimum_window_substring2(s:str,t:str)->str:
    """
    ##                  s
    ##   s "cabcwefgewcwaefgcf", t = "cae"
    ##                       e
    ##      left,right = 10,13
    ##      t-map = {c:1,a:1,e:1}
    ##      s-map = {c:1,a:1,e:1}
    ##      min-substr-len = 4
    ##      min-subtr = s[10:14] = "cwae"
    """
    n = len(s)
    left,right = [0]*2
    output = minimum_substr = ""
    t_char_freq = Counter(t)
    s_char_freq = {}
    while right < n:
        if s[right] in t_char_freq:
            if s[right] not in s_char_freq:
                s_char_freq[s[right]] = 1
            else:
                s_char_freq[s[right]] += 1
            if s[right] == s[left] and s_char_freq[s[right]] - t_char_freq[s[right]] > 0:
                # revalidate the window by moving the start index to the next
                # occurrence of a character that is also in string t.
                while s[left] not in t or s_char_freq[s[left]] - t_char_freq[s[left]] > 0:
                    if s[left] in t:
                        s_char_freq[s[left]] -= 1
                    left += 1
        if len(s_char_freq) == len(t_char_freq) and all([s_char_freq[char]-t_char_freq[char] >= 0 for char in t]):
            if not output:
                output = s[left:right+1]
            else:
                if right-left+1 < len(output):
                    output = s[left:right+1]
        right += 1
    return output

##   Time Complexity
"""
##   In the average-case scenario, each hash map operation will cost O(1). So, 
##   the time complexity for the above solution is O(n+m), where n and m are the 
##   lengths of the string s and t, respectively. This is because we're 
##   accessing each element of s at most once.
##   In the worst case, each hash map operation will cost O(m). Therefore, the 
##   overall time complexity is O(m + (n x m)).
##
"""
##   Space Complexity
"""
##   Since the characters in t are limited to uppercase and lowercase English 
##   letters, there is a maximum of 52 possible characters. Therefore, the size 
##   of the string and window hash maps will be at most 52, regardless of the 
##   length of t. Therefore, the space complexity of this solution will be O(1).
##
"""
