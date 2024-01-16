# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

##   Problem Statement
"""
##   Check whether or not a linked list contains a cycle. If a cycle exists 
##   return True. Otherwise, return False. The cycle means that at least one 
##   node can be reached again by traversing the next pointer.
##
##   Constraints:
##   * 0 <= n <= 500
##   * -10^5 <= node.data <= 10^5
##
##   Example 1:
##   Input: 2 -> 4 -> 6 -> 8 -> 10 ↩ 4
##   Output: True
##
##   Example 2:
##   Input: Head->1->3->5->7->9->NULL
##   Output: False
##
##   Example 3:
##   Input: Head->1->2->3->4->5->6 ↩ 4
##   Output: True
##
"""
##   Understand the Problem
"""
##   1. What is the output if the following linked list is given as input?
##   Input: 5->10->15->25->10
##   :: --> True
##
##   2. What is the output if the following linked list is given as input?
##   Input: 3->3->5->9->11->17 ↩ 9
##   :: --> True
##
##   3. What is the output if the following linked list is given as input?
##   Input: 9->9->9->9->9->9->9
##   :: --> False (slow and fast never point to same node)
##
"""
##   Arrange the Steps
"""
##   1. Initialize both fast and slow pointers to the head of the linked list.
##   2. Move the slow pointer by one and the fast pointer by two nodes 
##      forward.
##   3. Check if both pointers point to the same node at any point, if yes, 
##      then return True.
##   4. Else, if the fast pointer reaches the end of the linked list, returns 
##      False.
##
"""
##   Write the Solution Code
##   **Note**: The first input of the test case includes an array representing 
##   the contents of a build list. The second input represents the index of 
##   the node to which the tail pointer is pointing. It will be -1, in case it 
##   is pointing to NULL. The second input is not passed as a parameter in the 
##   function because it is just to represent the cycle in the linked list.

import random

mklist = lambda n: [random.randint(0,100) for i in range(n)]

def has_cycle(llst):
    slow,fast = llst._head or llst.head,llst._head or llst.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

class LinkedListNode():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        next_str = ''
        if self.next:
            next_str = ', ' + str(self.next)
        return f'LinkedListNode({str(self.data)}{next_str})'
    """
    def _detect_cycle(self):
        slow,fast = self,self
        while self and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    """
class LinkedList:
    def __init__(self):
        self._head = None
        self._length = 0
    """
    ##   Function to insert a node at the _head of the linked list  
    """
    def _insert(self,data):
        if not self._head:
            self._head = LinkedListNode(data)
        else:
            node = LinkedListNode(data)
            node.next = self._head
            self._head = node
        self._length += 1
    """
    ##   Method to create a linked list given an integer array.
    ##   This method uses the helper method _insert(), which
    ##   inserts a node at the _head of the linked list.
    """
    def _create_linked_list(self,lst):
        for data in reversed(lst):
            self._insert(data)
        return self
    """
    ##   Method to get the current number of nodes in the linked list.
    """
    def _get_length(self):
        return self._length
    """
    ##   Method to return the node at a specific position(index) in the linked 
    ##   list. 
    ##
    ##   **Use the sequence interface** i.e implement the following two 
    ##   methods:
    ##      1. __len__()
    ##      2. __getitem__()
    ##
    """
    def _get_node(self,index):
        return self[index]
    """
    ##   Method to detect if there is a cycle in the linked list.
    """
    def _detect_cycle(self):
        slow,fast = self._head,self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def __len__(self):
        return self._get_length()
    def __getitem__(self,index):
        if abs(index) > self._get_length()-1:
            raise IndexError('Index out of range')
        curr = self._head
        if index > 0:
            for i in range(index):
                curr = curr.next
        elif index < 0:
            temp = self._head
            for i in range(abs(index)):
                temp = temp.next
            while temp is not None:
                temp = temp.next
                curr = curr.next
        else:
            return curr
        return curr
    def __iter__(self):
        curr = self._head
        while curr is not None:
            yield curr
            curr = curr.next
    def __next__(self):
        curr = self._head
        if curr.next is not None:
            self = self.next
            return curr
        else:
            raise StopIteration
    def __str__(self):
        output = ''
        curr = self._head
        while curr:
            output += f'{curr.data}->'
            curr = curr.next
        output += 'NULL'
        return output

##   Solution Summary
"""
##   3-parts to the optimal solution:
##   1. Initialize both the slow and fast pointers to the head node.
##   2. Move both pointers at different rates i.e. the slow pointer will move 
##      one step ahead whereas the fast pointer will move two steps.
##   3. If both pointers are equal at some point, then a cycle exists.
##
"""
##   Time Complexity
"""
##   The time complexity of the algorithm is O(n), where n is the number of 
##   nodes in the linked list.
##
"""
##   Space Complexity
"""
##   The space complexity of the algorithm above is O(1).
##
"""
