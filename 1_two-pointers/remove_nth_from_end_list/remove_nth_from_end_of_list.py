# vim: set comments=sl\:\"\"\",m\:##\ \ \ \ ,ex-3\:\"\"\":
# vim: set fo=tcrq :
# vim: set comments=sb\:\"\"\",mb\:##\ \ \ \ ,ex-3\:\"\"\",\:##:
# vim: set fo=tcq1rowabvpn:

##    Problem Statement
"""
##    Given a singly linked list, remove the nth node from the end of the list 
##    and return its head.
##
##    Constraints:
##    * The number of nodes in the list is k.
##    * 1 <= k <= 10^4
##    * -10^3 <= Node.value <= 10^3
##    * 1 <= n <= Number of nodes in the list
##
##    Example 1:
##    Input: n = 1, lst = [43,68,11,5,69,37,70,NULL]
##    Output: [43,68,11,5,69,37,NULL]
##
##    Example 2:
##    Input: n = 3, lst = [23,28,10,5,67,39,70,NULL]
##    Output: [23,28,10,5,39,70,NULL]
##
##    Example 3:
##    Input: n = 5, lst = [1,2,3,4,5,6,7,NULL]
##    Output: [1,2,4,5,6,7,NULL]
##
##    Example 4:
##    Input: n = 4, lst = [50,40,30,20,NULL]
##    Output: [10,30,20,NULL]
##
"""
##    Understand the Problem
"""
##    1. What is the output if the following linked list and value of n are 
##       given as input?
##       LinkedList: 32->78->65->90->12->44->NULL, n = 3
##       :: 32->78->65->12->44->NULL
##    2. What is the output if the following linked list and value of n are 
##       given as input?
##       LinkedList: 12->15->13->16->17->14->NULL, n = 5
##       :: 12->13->16->17->14->NULL
##    3. What is the output if the following linked list and value of n are 
##       given as input?
##       LinkedList: 10->20->30->40->50->60->NULL, n = 6
##       :: 20->30->40->50->60->NULL
##
"""
##    Arrange the Steps
"""
##    1. Set two pointers, right and left, at the head of the linked list.
##    2. Move the right pointer forward n steps.
##    3. Move both the right and left pointers forward untul the right pointer 
##       reaches the last node (before NULL). At this point, the left pointer 
##       will be pointing to the node just before the nth node from the end of 
##       the list.
##    4. Relink the left node to the node next to left's next node (i.e 
##       left.next.next).
##    5. Return the head of the linked list.
##
"""
##    Write the Solution Code
from collections.abc import Sequence
class LinkedListNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __repr__(self):
#        result = ''
#        temp = self
#        while temp:
#            result += f'{temp.data}->'
#            temp = temp.next
#        result += 'NULL'
#        return result
        if self.next:
            rest_str = ', ' + repr(self.next)
        else:
            rest_str = ''
        return f'LinkedListNode({repr(self.data)}{rest_str})'
    def __str__(self):
        result = ''
        temp = self
        while temp:
            result += f'{temp.data}->'
            temp = temp.next
        result += 'NULL'
        return result
class LinkedList():
    def __init__(self):
        self.head = None
    def insert_node_at_head(self,node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    def create_linked_list_from_list(self,lst):
        for i in reversed(lst):
            new_node = LinkedListNode(i)
            self.insert_node_at_head(new_node)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def __next__(self):
        node = self.head
        if node.next is not None:
            self = self.next
            return node
        else:
            raise StopIteration
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += f'{temp.data}->'
            temp = temp.next
        result += "NULL"
        return result
def remove_nth_node_from_end(head:LinkedListNode, n:int)->LinkedListNode|None:
    """
    ##    Input: n = 5, lst = [1,2,3,4,5,6,7,NULL]
    ##           i = 5         ^         ^
    ##           while i < n ...
    ##           while right.next ...
    """
    # if head is None, LinkedList is empty 
    if not head: return None
    # assign left and right pointers
    left,right = head,head
    # move right pointer while less than n
    for i in range(n):
        right = right.next
    # if right reaches NULL after moving n steps,
    # then node to remove is head itself, i.e return head.next
    #if not right:
    #    return head.next
    # move both pointers while right.next
    while right and right.next:
        right = right.next
        left = left.next
    # if left equals head and right is NULL, 
    # then node to remove is head itself
    if left == head and not right:
        head = left.next
    else:
    # set left.next to left.next.next
        left.next = left.next.next
    return head

##   Solution Summary
"""
##    1. Two pointers, left and right are set to the head node.
##    2. Move the right pointer n steps forward
##    3. If right reaches NULL, then the node to remove is head itself. Return 
##       head's next node (i.e head.next).
##    4. Move both left and right pointers forward until right reaches the 
##       last node (i.e while right.next)
##    5. ReLink/point left's next pointer to left's next's next node (i.e 
##       left.next.next)
##    6. Return the original head node.
##    
"""
##    Time Complexity
"""
##    The time complexity is O(n), where n is the number of nodes in the 
##    linked list.
##
"""
##    Space Complexity
"""
##    The space complexity is O(1), since we use constant space to store two 
##    pointers.
##
"""
