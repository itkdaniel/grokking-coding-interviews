# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

##   Test Cases
"""
##   Input Format:
##   param 1: list[]
##   param 2: *Not really a param input, used to represent cycle on index/node
##            x* Or -1 if NULL
##   
##   Test Case 1:
##   Input: [2,4,6,8,10], 2
##   Output: True
##
##   Test Case 2:
##   Input: [1,3,5,7,9], -1
##   Output: False
##
##   Test Case 3:
##   Input: [1,2,3,4,5], 3
##   Output: True
##
##   Test Case 4:
##   Input: [0,2,3,5,6], -1
##   Output: False
##
##   Test Case 5:
##   Input: [3,6,9,10,11], 0
##   Output: True
##
"""
import unittest
# import pytest
from linked_list_cycle import LinkedListNode
from linked_list_cycle import LinkedList
from linked_list_cycle import has_cycle

def make_cycle(lst,index):
    curr = lst._head
    if index >= 0:
        lst[-1].next = lst[index]

class TestLinkedListCycle(unittest.TestCase):
    def test_case_1(self):
        input = ([2,4,6,8,10], 2)
        expected = True
        llst = LinkedList()._create_linked_list(input[0])
        make_cycle(llst,input[1])
        self.assertTrue(llst._detect_cycle())
    def test_case_2(self):
        input = ([1,3,5,7,9], -1)
        expected = False
        llst = LinkedList()._create_linked_list(input[0])
        self.assertFalse(llst._detect_cycle())
    def test_case_3(self):
        input = ([1,2,3,4,5], 3)
        expected = True
        llst = LinkedList()._create_linked_list(input[0])
        make_cycle(llst,input[1])
        self.assertTrue(llst._detect_cycle())
    def test_case_4(self):
        input = ([0,2,3,5,6], -1)
        expected = False
        llst = LinkedList()._create_linked_list(input[0])
        self.assertFalse(llst._detect_cycle())
    def test_case_5(self):
        input = ([3,6,9,10,11], 0)
        expected = True
        llst = LinkedList()._create_linked_list(input[0])
        make_cycle(llst,input[1])
        self.assertTrue(llst._detect_cycle())

if __name__ == '__main__':
    unittest.main(verbosity=2)
