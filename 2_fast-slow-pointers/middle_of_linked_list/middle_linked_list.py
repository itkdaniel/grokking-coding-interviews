# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1ropn:

##   Problem Statement
"""
##   Given the head of a singly linked list, return the middle node of the
##   linked list. If the number of the nodes in the linked list is even, there
##   will be two middle nodes, so return the second one.
##
##   Constraints:
##   * head != NULL
##
##   Example 1:
##   Input: 1->2->3->4->5->NULL
##   Output: 3
##
##   Example 2:
##   Input: 1->2->3->4->5->6->NULL
##   Output: 4
##
##   Example 3:
##   Input: 1->2->NULL
##   Output: 2
##
"""
##   Understand the Problem
"""
##   1. What is the output if the following linked list is given as input?
##      2->4->6->8->10->NULL
##      :: -> 5
##
##   2. What is the output if the following linked list is given as input?
##      1->3->5->7->9->11->NULL
##      :: --> 7
##
##   3. What is the output if the following linked list is given as input?
##      16->NULL
##      :: --> 16
##
"""
##   Arrange the Steps
"""
##   1. Create and initialize two pointers, slow and fast, both set to the head
##   of the linked list.
##   2. Traverse the linked list while moving the slow pointer one step
##      forward while moving the fast pointer two steps forward.
##   3. When the fast pointer reaches the last node or NULL, the slow pointer
##      will point to the middle node of the linked list.
##   4. Return the node that slow pointer points to.
##
"""
##   Write the Solution Code
class LinkedListNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        next_str = ''
        if self.next:
            next_str += ', ' + str(self.next)
        return f'LinkedListNode({str(self.data)}{next_str})'

class LinkedList:
    def __init__(self):
        self._head = None
        self.length = 0
    """
    ##   Method to insert data at the front/beginning of the linked list.
    """
    def _insert(self,data):
        if not self._head:
            self._head = LinkedListNode(data)
        else:
            new_node = LinkedListnode(data,self._head)
            self._head = new_node
        self._get_length()
    """
    ##   Method to create a linked list given an array. It uses the helper
    ##   method, _insert(data), to insert elements to the front of the linked
    ##   list.
    ##
    """
    def _create_linked_list(self,lst)->LinkedListNode:
        for i in reversed(lst):
            self._insert(i)
        return self
    """
    ##   Method returns the length of the linked list.
    ##   
    """
    def _get_length(self):
        return self._length
    """
    ##   Method to detect if linked list contains a cycle.
    ##
    """
    def _has_cycle(self):
        slow,fast = self._head,self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    """
    ##   Method to get the middle node in the linked list.
    ##   If the length of the linked list is even, return the second of the
    ##   two middle nodes.
    ##
    """
    def _get_middle_node(self):
        slow,fast = self._head,self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    """
    ##   Method to reverse a linked list.
    ##
    """
    def _reverse_linked_list(self):
        prev,curr = None,self._head
        while curr:
            curr.next = prev
            prev = curr
            curr = next
        return prev
    """
    ##
    ##   Method returns a node at a specific index/position.
    ##   
    ##   Note: Requires the sequence protocol/interface to be implemented.
    """
    def _get_node(self,index):
        return self[index]
    def __len__(self):
        return self._get_length()
    def __getitem__(self,index):
        curr = self._head
        if abs(index) > self._get_length()-1:
            raise IndexError(f'Index out of range. Trying to access {index=},
            but length={self._lengt}')
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
        output += 'NULL'
        return output




class LinkedList:
      def __init__(self):
              self.head = None
              self._length = 0
      def _insert(self,data):
              if not self.head:
                      self.head = LinkedListNode(data)
              else:
                      node = LinkedListNode(data)
                      node.next = self.head
                      self.head = node
              self._length += 1
      def _get_node(self,index):
          return self[index]
      def __len__(self):
              return self._length
      def _create_linked_list(self,lst):
              for i in reversed(lst):
                      self._insert(i)
      def __getitem__(self,index):
              curr = self.head
              if index > self._length-1:
                  raise IndexError('Index out of range')
              if index > 0:
                 for i in range(index):
                          curr = curr.next
              elif index < 0:
                  temp = self.head
                  if abs(index) > self._length:
                      raise IndexError('Index out of range')
                  for i in range(abs(index)):
                      temp = temp.next
                  while temp is not None:
                      temp = temp.next
                      curr = curr.next
              else:
                  return curr.data
              return curr.data
      def __str__(self):
              output = ''
              curr = self.head
              while curr:
                      output += f'{str(curr.data)}->'
                      curr = curr.next
              output += f'->NULL'
              return output
      def __iter__(self):
              node = self.head
              while node is not None:
                      yield node
                      node = node.next
      def __next__(self):
              curr = self.head
              if curr.next is not None:
                      self = self.next
                      return curr
              else:
                      raise StopIteration
      def _get_middle_node(self):
               slow,fast = self.head,self.head
               while fast and fast.next:
                       slow = slow.next
                       fast = fast.next.next
                       return slow.next
               if self._length % 2 == 0:
                   return slow.next
               return slow
               
