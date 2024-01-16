# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Problem Statement
"""
##   Given the head of a linked list, your task is to check whether the linked 
##   list is a palindrome or not. Return TRUE if the linked list is a palindrome;
##   otherwise return FALSE.
##
##   **Note**: The input linked list prior to the checking process should be 
##   identical to the list after the checking process has been completed. 
##
##   Constraints:
##   * Let n be the number of nodes in a linked list.
##   * 0 <= Node.value <= 9
##
##   Example 1:
##   Input: 2->4->6->4->2->NULL
##   Output: True
##
##   Example 2:
##   Input: 0->3->5->5->0->NULL
##   Output: False
##
##   Example 3:
##   Input: 9->7->4->4->7->9->NULL
##   Output: True
##
"""
##   Understand the Problem
"""
##   Q: What is the output if the following linked lists are provided as input?
##   
##   1. Input: 7->3->3->3->7
##   :: Output: True
##   
##   2. Input: 1->2->3->4->4->5->5->3->2->1
##   :: Output: False
##
##   3. Input: 8->5->6->0->1->0->6->5->8
##   :: Output: True
##
##   4. Input: 1->1->1->0->0->1->1->1
##   :: Output: True
##
"""
##   Arrange the Steps
"""
##   1. Initialize the slow and fast pointers to the head of the linked list.
##   2. Traverse the linked list using both pointers at different speeds. At 
##      each iteration, the slow pointer increments by one node, and the fast 
##      pointer increments by two nodes.
##   3. Continue doing so until the fast pointer reaches the end of the linked 
##      list. At this point, the slow pointer will be pointing to the middle 
##      of the linked list.
##   4. Reverse the second half of the linked list and compare it with the 
##      first half.
##   5. If both halves of the list match, the linked list is 
##      a palindrome, return True. Otherwise, it is not and return False.
##
"""
##   Write the Solution Code
class LinkedListNode:
    """
    ##   A class that represents a Linked List Node object.
    """
    def __init__(self, value): 
        self.value = value
        self.next = None
    
    def __str__(self):
        next_str = ''
        if self.next is not None:
            next_str = ', ' + str(self.next)
        return f'LinkedListNode({str(self.value)}{next_str})'

    def reverse(self):
        prev = None
        current = self
        while current:
            next_node,current.next = current.next,prev
            prev,current = current,next_node
        return prev
                        
class LinkedList:
    """ 
    ##   A class that represents the Linked List. It only points to the root 
    ##   node which is the head of the linked list.
    """
    def __init__(self):
        self.head = None
    
    def __str__(self):
        output = ''
        curr = self.head
        while curr:
            output += f'{curr.value}->'
            curr = curr.next
        if curr is None:
            output += 'NULL'
        return output
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def add_node(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_node(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def create_linked_list(self,lst):
        for i in reversed(lst):
            self.insert_node(i)
        return self
    def is_palindrome(self):
        slow,fast,start = [self.head]*3
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.reverse()
        temp = slow
        while temp and start:
            if temp.value != start.value:
                slow.reverse()
                return False
            temp,start = temp.next,start.next
        slow.reverse()
        return True

import random
class LinkedListManager:
    @staticmethod
    def create_linked_list(lst):
        ll = LinkedList().create_linked_list(lst)
        return ll
    @classmethod
    def generate_linked_list(cls,r=6,l=0,u=100):
        lst = [random.randint(l,u) for i in range(r)]
        ll = cls.create_linked_list(lst)
        return ll
    @staticmethod
    def reverse_linked_list(node):
        prev_node = None
        current_node = node
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node
    @classmethod
    def is_palindrome(cls,lst):
        """
        def check(slow,start):
            while slow and start:
                if slow.value != start.value:
                    return False
                slow,start = slow.next,start.next
            return True
        slow,fast,start = [lst.head]*3
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        slow = cls.reverse_linked_list(slow)
        pcheck = check(slow,start)
        cls.reverse_linked_list(slow)
        if pcheck:
            return True
        return False
        """
        def check(slow,start):
            while slow and start:
                if slow.value != start.value:
                    return False
                slow,start = slow.next,start.next
            return True
        slow,fast,start = [lst.head]*3
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        slow = cls.reverse_linked_list(slow)
        pcheck = check(slow,start)
        cls.reverse_linked_list(slow)
        if pcheck:
            return True
        return False

def reverse_linked_list(node:'LinkedListNode'):
    """
    ##   A function to reverse the linked list starting at any given node in 
    ##   the linked list.
    ##
    ##   1->2->3->4->5->NULL
    ##   p = NULL
    ##   c = 1->2->rest
    ##
    ##   nxtn = 2->3->rest
    ##   1->NULL
    ##   p = 1->NULL
    ##   c = 2->3->rest
    ##
    ##   nxtn = 3->4->rest
    ##   2->1->NULL
    ##   p = 2->1->NULL
    ##   c = 3->4->rest
    ##
    ##   nxtn = 4->5->NULL
    ##   3->2->1->NULL
    ##   p = 3->2->1->NULL
    ##   c = 4->5->NULL
    ##
    ##   nxtn = 5->NULL
    ##   4->3->2->1->NULL
    ##   p = 4->3->2->1->NULL
    ##   c = 5->NULL
    ##
    ##   nxtn = NULL
    ##   5->4->3->2->1->NULL
    ##   p = 5->4->3->2->1->NULL
    ##   c = NULL
    ##
    ##   ret p = 5->4->3->2->1->NULL
    """
    prev_node = None
    current_node = node
    while current_node:
        next_node,current_node.next = current_node.next,prev_node
        prev_node,current_node = current_node,next_node
    return prev_node

def is_palindrome(head:'LinkedListNode')->bool:
    """
    ##   A function to determine if a linked list is a valid palindrome given 
    ##   the root (head) node of the linked list. The function returns True or 
    ##   False for is and is not a valid palindrome respectively.
    """
    slow,fast,start = [head]*3
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = reverse_linked_list(slow)
    temp = slow
    while temp and start:
        if temp.value != start.value:
            return False
        temp,start = temp.next,start.next
    reverse_linked_list(slow)
    return True

##   Time Complexity
"""
##   The time complexity of this algorithm is O(n), where n is the total 
##   number of nodes in the linked list.
##
"""
##   Space Complexity
"""
##   The space complexity of this algorithm is O(1), since it does not use any 
##   additional data structures or memory.
##
"""
