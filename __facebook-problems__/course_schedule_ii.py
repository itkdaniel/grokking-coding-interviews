# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Course Schedule II

##   Problem Statement
"""
Given the total number of courses n and a list of the prerequisite pairs, return 
the course order a student should take to finish all of the courses. If there 
are multiple valid orderings of course, then return any one of them.

Example 1:
    Input: prereqs = [[1,0],[2,0],[3,1],[4,3]], n = 5
    Output: [0,1,2,3,4] OR [0,2,1,3,4]
"""
##   Arrange the Steps
"""
##   1. Create a graph with a node for each course and edges representing the 
##      dependencies. Store the in-degrees of each node in a separate data 
##      structure.
##   2. Pick a node with in-degree equal to zero and add it to the output list.
##   3. Decrement the in-degree of the node picked in the previous step.
##   4. Repeat for all nodes with in-degree equal to zero.
##
"""
##   Write the Solution
def find_order(n, prerequisites):
    sorted_order = []
    if n <= 0:
        return sorted_order
    in_degree = {i:0 for i in range(n)}
    graph = {i: [] for i in range(n)}

    for prequisite in prerequisites:
        parent,child = prerequisite[1], prerequisite[0]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    if len(sorted_order) != n:
        return []
    return sorted_order
