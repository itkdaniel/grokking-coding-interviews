# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Verifying an Alien Dictionary

##   Problem Statement
"""
##   Given a list of words with lowercase English letters in a different order, 
##   written in an alien language. The order of the alphabet is some permutation 
##   of lowercase letters of the English lanuage.
##
##   Return TRUE if the given list of words is sorted lexicographically in this 
##   alien language.
##
##   Constraints:
##   * 1 <= woreds.length <= 10^3
##   * 1 <= words[i].length <= 20
##   * order.length == 26
##   * All the characters in words[i] and order are lowercase English letters.
##
##   Example 1:
##   Input: words = ['coding', 'interview'], order = 'abcdiefghjklmnorpqstuvwxyz'
##   Output: True
##   Explanation: As 'c' precedes 'i' in the order, the words are 
##   lexicographically sorted.
##
##   Example 2:
##   Input: words = ['educated', 'educate'], order = 'educatbfghijklmnopqrsvwxyz'
##   Output: False
##   Explanation: Conversly, the first 7 letters of 'educate' match, and the 
##              second word is shorter in size. Since 'educated' > 'educate', because 'd' 
##              > '@', where '@' is defined as the blank character, which is less than any 
##              other character.
##
"""
##   Algorithm Steps
"""
##   1. Fill the hash map with each character of the order string and its 
##      adjacent index.
##   2. Iterate a word list.
##   3. Iterate words[i] string and compare each character with the character of 
##      an adjacent word from the list, words[i+1].
##          - if there is no different character in the selected words, and the 
##          words[i+1] end before words[i], return FALSE.
##          - If there is a different character and the two selected words are 
##          in the correct order, we move to the next two adjacent words.
##          - If there is a different character and the two words are not in the 
##          correct order, return FALSE.
##          - If the loop ends after iterating all of the words, return TRUE.
##
"""
##   Arrange the Steps
"""
##   1. Store the ranking of each letter from the order string in the data 
##      structure.
##   2. Iterate over the 2 adjacent words in the words list.
##   3. If length of words[i+1] is less than length words[i], return FALSE.
##   4. Else if, the characters in both of the words are different and words are 
##      in correct order, exit and move to the next two adjacent words.
##   5. Else, return FALSE if the characters are different in both words and 
##      words are not in correct order.
##   6. At the end of the loop, all of the adjacent words have been examined, 
##      which ensures that all of the words are sorted. Therefore, return TRUE.
##
"""
##   Write the Solution
def verify_alien_dictionary(words, order):
    if len(words) == 1:
        return True
    
    order_map = {}

    for index,val in enumerate(order):
        order_map[val] = index

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if len(words[i+1]) <= j:
                return False
            if words[i][j] != words[i+1][j]:
                if order_map[words[i][j]] > order_map[words[i+1][j]]:
                    return False
                break
    return True

