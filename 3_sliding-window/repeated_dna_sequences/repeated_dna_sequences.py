# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

## Repeated DNA Sequences

##   Problem Statement
"""
##   Given a string, s, that represents a DNA subsequence, and a number k, 
##   return all the contiguous subsequences (substrings) of length k that 
##   occur more than once in the string. The order of the returned 
##   subsequences does not matter. If no repeated substring is found, the 
##   function should return an empty set.
##
##   **Note**: The DNA sequence is composed of a series of nucleotides 
##   abbreviated as A,C,G,T. For example, ACGAATTCCG, is a DNA sequence. When 
##   studying DNA, it is useful to identify repeated sequences in it.
##
##   Constraints:
##   * 1 <= s.length <= 10^4
##   * s[i] is either A,C,G,T
##   * 1 <= k <= 10
##
##   Example 1:
##   Input: k = 3, s = "GAGTCACAGTAGTTTCA"
##   Output: ["AGT","TCA"]; "G[AG[T]CA]C[AGT][AGT]T[TCA]"
##
##   Example 2:
##   Input: k = 7, s = "CAAACCCCGTAAACCCCA"
##   Output: ["AAACCCC"]
##
##   Example 3:
##
"""
##   Arrange the Steps
"""
##   1. Iterate over the k-length substrings of the input string.
##   2. Store the hash of the current substring to keep track of all unique 
##      substrings.
##   3. If the hash of a substring has already been stored, the substring is 
##      repeated, so we add it to the output.
##   4. When all substrings have been evaluated, return the output.
##
"""
##   Write the Solution Code
def find_repeated_sequences(s:str, k:int)->set:
    output,seen = set(),set()
    left,right = 0,0+k
    n = len(s)
    while right < n:
        current_sequence = hash(s[left:right])
        if current_sequence in seen:
            output.add(s[left:right])
        seen.add(current_sequence)
        left,right = left+1,right+1
    return output

def find_repeated_sequences_polyroll_hashing(s:str,k:int)->set:
    output,seen = set(),set()
    n,a = len(s),4
    if n < k:
        return set([])
    mapping = {'A':1,'C':2,'G':3,'T':4}
    numbers = [mapping.get(s[i]) for i in range(n)]
    current_hash = 0
    for i in range(n-k+1):
        if i == 0:
            for j in range(k):
                # hash_value = sum([C[j]*(a**(k-j)) for j in range(k)])
                current_hash += numbers[j]*(a**(k-j-1))
        else:
            prev_hash = current_hash
            current_hash = ((prev_hash-numbers[i-1]*(a**(k-1)))*4) + numbers[i+k-1]
        if current_hash in seen:
            output.add(s[i:i+k])
        seen.add(current_hash)
#        print(f'\tHash value of {s[i:i+k]}: {current_hash}' +
#              f'\n\tSeen: {seen}' +
#              f'\n\tOutput: {output}\n')
    return output

##   Solution Summary
"""
##   1. Iterate over all k-length substrings.
##   2. Compute the hash value for the contents of the sliding window.
##   3. Add the hash value to the set that tracks the hashes of all substrings 
##      of the given length k.
##   4. Slide the window one step forward and compute the hash of the new 
##      window using the polynomial rolling hashing method.
##   5. If the hash value has already been seen, the sequence in the current 
##      window is repeated, so we add it to the output set/array.
##   6. Once all substrings have been evaluated, return the output set/array.
##
"""
##   Time Complexity
"""
##   The average time complexity of this solution is O(n), where n is the 
##   length of the input string. It is calculated as follows:
##     - Time taken to populate the numbers array: O(n)
##     - Time taken to traverse all k-length substrings: O(n-k-1)
##     - Time taken to calculate the hash value of a k-length substring: O(1)
##   Therefore, the dominating time complexity becomes O(n).
##
##   Worst Case:
##   Consider the worst case time complexity of this solution, considering the 
##   input string "AAAAAAAA" with k = 2. This combination of inputs ensures 
##   that a repeated sequence "AA" is detected and added to the output each 
##   time the window slides forward. Therefore, we must generate a k-length 
##   substring on each (n-k-1) iteration of the loop. The time to generate 
##   a k-length substring is O(k). Therefore, the overall time complexity then 
##   becomes O((n-k)*k).
##
"""
##   Space Complexity
"""
##   The space complexity of this solution is O(n). 
##     - Space occupied by the mapping hashmap: O(1)
##     - Space occupied by the numbers array: O(n)
##     - Space occupied by the seen set: O(n-k-1)
##   Therefore, the dominating space complexity becomes O(n).
##
"""
