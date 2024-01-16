# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Alien Dictionary

##   Problem Statement
"""
##   Given a list of words written in the alien language, you have to return 
##   a string of unique letters sorted in the lexicographical order of the alien 
##   lanuguage as derived from the list of words.
##
##   If there is no solution, i.e no lexicographical ordering, return an empty 
##   string.
##
##   **Note**: The lexicographic order of a given language is defined by the 
##   order in which the letters of its alphabet appear. In English, the letter 
##   "n" appears before the letter "r" in the alphabet. As a result, in two 
##   words that are the same up to the point where one features "n" and the 
##   other features "r", the former is considered the lexicographically smaller 
##   word of the two. For this reason, "ban", is considered lexicographically 
##   smaller than "bar".
##   Similarly, if an input contains words followed by their prefix, such as 
##   "educated" and then "educate", these cases will never result in a valid 
##   alphabet because in a valid alphabet, prefixes are always first.
##
##   Constraints:
##   * 1 <= words.length <= 20
##   * 1 <= words[i].length <= 20
##   * All characters in words[i] are English lowercase letters.
##
##   Example 1:
##   Input: words = ["ba", "ba", "ba"]
##   Output: order = "ab"
##
##   Example 2:
##   Input: words = ["world", "hello", "world"]
##   Output: ""
##
##   Example 3:
##   Input: words = ["xro","xma","per","pert","oxh"]
##   Output: "artevxhmplo"
##
"""
##   Arrange the Steps
"""
##   1. Build the graph from the input using adjacency lists.
##   2. Remove the source, i.e verticies with indegree = 0 from the graph and 
##      add them to a results array.
##   3. Decrement the indegree of the sources children by 1.
##   4. Repeat until all nodes are visited.
##
"""
##   Write the Solution Code
"""
##   Optimized Approach: Topological Sort
##   Find a linear ordering of elements that have dependencies on or priority 
##   over each other. For example, if A is dependent on B or B has priority over 
##   A, then B is listed before A in topological order.
##
##   Generate a graph by identifying the relative precendence order of the 
##   letters in the words. Traverse the graph using BFS to find the letters' 
##   order.
##
"""
##   Step by Step Solution Construction
"""
##   1. Build a graph from the given word and keep track of the in-degrees of 
##      alphabets in a dictionary.
##   2. Add the sources to a result list
##   3. Remove the sources and update the in-degrees of their children. If the 
##      in-degree of a child becomes 0, its the next source.
##   4. Repeat until all alphabets are covered.
##
"""
from collections import defaultdict, Counter, deque   
def alien_order(words):
    graph = defaultdict(set)
    counts = Counter({c: 0 for word in words for c in word})
    outer = 0

    for word1, word2 in zip(words,words[1:]):
        outer += 1
        inner = 0
        for c,d in zip(word1, word2):
            inner += 1
            if c != d:
                if d not in graph[c]:
                    graph[c].add(d)
                    counts[d] += 1
                break
        else:
            if len(word2) < len(word1):
                return ""
    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)

        for d in graph[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)
    if len(result) < len(counts):
        return ""
    return "".join(result)

