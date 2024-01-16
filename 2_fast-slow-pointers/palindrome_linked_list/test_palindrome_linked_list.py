# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   Test Case 1:
##   Input: [1,2,3,2,1]
##   Output: True
##
##   Test Case 2:
##   Input: [4,7,9,5,4]
##   Output: False
##
##   Test Case 3:
##   Input: [2,3,5,5,3,2]
##   Output: True
##
##   Test Case 4:
##   Input: [6,1,0,5,1,6]
##   Output: False
##
##   Test Case 5:
##   Input: [3,6,9,8,4,8,9,6,3]
##   Output: True
##
"""

import unittest
from palindrome_linked_list import (
        LinkedListManager,
        LinkedListNode,
        LinkedList,
        reverse_linked_list,
        is_palindrome
)

class TestPalindromeLinkedList(unittest.TestCase):
    def setUp(self):
        self.llm = LinkedListManager()
    def test_case_1(self):
        input = [1,2,3,2,1]
        expected = True
        self.assertTrue(self.llm.is_palindrome(self.llm.create_linked_list(input)))
    def test_case_2(self):
        input = [4,7,9,5,4]
        expected = False
        self.assertFalse(self.llm.is_palindrome(self.llm.create_linked_list(input)))
    def test_case_3(self):
        input = [2,3,5,5,3,2]
        expected = True
        self.assertTrue(self.llm.is_palindrome(self.llm.create_linked_list(input)))
    def test_case_4(self):
        input = [6,1,0,5,1,6]
        expected = False
        self.assertFalse(self.llm.is_palindrome(self.llm.create_linked_list(input)))
    def test_case_5(self):
        input = [3,6,9,8,4,8,9,6,3]
        expected = True
        self.assertTrue(self.llm.is_palindrome(self.llm.create_linked_list(input)))

if __name__ == '__main__':
    unittest.main(verbosity=2)
