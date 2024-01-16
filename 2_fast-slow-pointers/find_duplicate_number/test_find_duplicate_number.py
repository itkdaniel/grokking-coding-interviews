# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##  Test Cases 
"""
##   Example 1:
##   Input: [1,3,3,4,2,5]
##   Output: 3
##
##   Example 2:
##   Input: [1,5,3,4,2,5]
##   Output: 5
##
##   Example 3:
##   Input: [1,2,3,4,5,6,6,7]
##   Output: 6
##
##   Example 4:
##   Input: [4,6,7,7,3,5,2,8,1]
##   Output: 7
##
##   Example 5:
##   Input: [9,8,7,6,2,3,5,4,1,9]
##   Output: 9
##
"""
##   Arrange the Steps
"""
##   1. Traverse nums using two pointers, slow and fast, initially set at the 
##      start index; 0.
##   2. Move the pointers until they meet. The slow pointer moves once and the 
##      fast pointer moves twice as fast as the slow pointer.
##   3. After the pointers meet, traverse nums once again.
##   4. Move the slow pointer from the start of nums and the fast pointer from 
##      the meeting point at the same speed (one step) until they meet again.
##   5. Return the fast pointer.
##
"""  
##   Write the Solution Code
import unittest
import find_duplicate_number as fdn

class TestDuplicateNumber(unittest.TestCase):
    def test_case_1(self):
        input = [1,3,3,4,2,5]
        expected = 3
        self.assertEqual(fdn.find_duplicate_number(input), 3)
    def test_case_2(self):
        input = [1,5,3,4,2,5]
        expected = 5
        self.assertEqual(fdn.find_duplicate_number(input), 5)
    def test_case_3(self):
        input = [1,2,3,4,5,6,6,7]
        expected = 6
        self.assertEqual(fdn.find_duplicate_number(input), 6)
    def test_case_4(self):
        input = [4,6,7,7,3,5,2,8,1]
        expected = 7
        self.assertEqual(fdn.find_duplicate_number(input), 7)
    def test_case_5(self):
        input = [9,8,7,6,2,3,5,4,1,9]
        expected = 9
        self.assertEqual(fdn.find_duplicate_number(input), 9)
    def test_case_x(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
