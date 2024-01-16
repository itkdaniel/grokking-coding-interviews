# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowan:

##   Problem Statement
"""
##   Given a sentence, reverse the order of its words without affecting the
##   order of letters within a given word.
##
##   Constraints:
##   * Sentence contains English uppercase and lowercase letters, digits, and
##   spaces.
##   * 1 <= sentence.length <= 10^4
##   * The order of the letters within a word is not to be reversed.
##
##   **Note**: The string may contain leading or trailing spaces or multiple
##   spaces between words. The returned string, however, should only have
##   a single space separating each word. Do not include any extra spaces.
##
##   Example 1:
##   Input: string = "Hello Friend"
##   Output: "Friend Hello"
##
##   Example 2:
##   Input: string = "Welcome to Educative"
##   Output: "Educative to Welcome"
##
##   Example 3:
##   Input: string = "Hurray 3 2 1"
##   Output: "1 2 3 Hurray"
##
"""
##   Understand the Problem
"""
##   1. What should be the output if the following sentence is given as input?
##   string = "The quick brown fox jumped over a lazy dog"
##   :: --> "dog lazy a over jumped fox brown quick The"
##
##   2. What should be the output if the following sentence is given as input?
##   string = "Educative Answers"
##   :: --> "Answers Educative"
##
##   3. What should be the output if the following sentence is given as input?
##   string = "practice problems to improve your coding"
##   :: --> "coding your improve to problems practice"
##
##   4. What should be te output if the following sentence is given as input?
##   string = "Reverse the words in a sentence"
##   :: --> "sentence a in words the Reverse"
##
"""
##   Arrange the steps
"""
##   1. Reverse the entire string.
##   2. Start iterating over the reversed string using two pointers, start and
##      end, initially set at index 0.
##   3. While iterating over the string, when end points to a space, reverse
##      the word pointed to by start and end-1
##   4. Once the word has been reversed, update the start and end to the start
##      index of the next word.
##   5. Repeat the process until the entire string is iterated and return the
##      string.
##
"""
import re

##   Approach 1:
##   Reverses the original string in each iteration
##   In each iteration, since the reversed string is not saved initially, 
##   reverse the string again, then reverse the current word in that reversed 
##   string and add the reversed word to the output string. After the 
##   iteration finished, reverse the last word in the reversed string and add 
##   it to the output string. Finally, return the output string.
##
##   Time Complexity:
##   The function reverses the string in every iteration, which is O(n^2).  
##   Additionally, for every iteration, it reverses the string again, then 
##   reverses the current word in the reversed string, which is an O(n+m) 
##   operation. So the time complexity is O(n^2^(n+m)).
##
##   Space Complexity:
##   The space complexity is O(n) since it stores the output in a new output 
##   string.
def reverse_sentence_1(s:str)->str:
     n = len(s)
     i,j = 0,0
     r = ''
     while j < n:
         if ''.join(reversed(s))[j] == ' ':
             r += ''.join(reversed(''.join(reversed(s))[i:j])).strip() + ' '
             i = j
         j += 1
     r += ''.join(reversed(''.join(reversed(s))[i:j])).strip()
     return r

##   Approach 2:
##   The function stores the reversed string before beginning iteration. Then 
##   , it reverses each word in the stored reverse string.  After iteration 
##   completes, it reverses the last word in the stored reversed string.  
##   Finally, returns the output string.
##
##   Time Complexity:
##   Stores the reversed string before beginning iteration.
##   Then it iterates the reversed string at most once while reversing each 
##   word in the reversed string. So the time complexity is O(n).
##
##   Space Complexity:
##   Since the function stores the reversed string in a new string, and also 
##   uses another string to store the output string, the space complexity is 
##   O(n).
def reverse_sentence_2(s:str)->str:
     n = len(s)
     i,j = 0,0
     r = ''
     s = ''.join(reversed(s))
     while j < n:
         if s[j] == ' ':
             r += ''.join(reversed(s[i:j])).strip() + ' '
             i = j
         j += 1
     r += ''.join(reversed(s[i:j])).strip()
     return r

##   Approach 3:
##   The function iterates the entire string once to first reverse the entire 
##   string, which is O(n). Then iterates the reversed string once again to 
##   reverse each word in the string. Which is O(n).  Finally, returns the 
##   original string containing all words in reversed order.
##
##   Time Complexity:
##   The time complexity is O(n), since it traverses the string at most once.
##
##   Space Complexity:
##   The space complexity is O(n), linear because it copies the string to 
##   a list to overcome immutability if Python strings.
def reverse_sentence(s:str)->str:
    s = re.sub(' +', ' ', s).strip()
    s = list(s)
    n = len(s)
    start,end = 0,n-1
    # reverse entire string
    while start < end:
       s[start],s[end] = s[end],s[start]
       start += 1
       end -= 1
    start,end = 0,0
    # reverse each word in the reversed string list
    while end < n:
        if s[end] == ' ':
            temp = end-1
            while start < temp:
                s[start],s[temp] = s[temp],s[start]
                start += 1
                temp -= 1
            start = end+1
        end += 1
    # reverse the last word in the sstring
    while start < end:
        s[start],s[end-1] = s[end-1],s[start]
        start += 1
        end -= 1
    return ''.join(s)          
