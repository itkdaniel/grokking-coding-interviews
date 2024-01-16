# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

##   Test Cases
"""
##   Test Case 1:
##   Input: 2147483646
##   Expected: False
##
##   Test Case 2:
##   Input: 1
##   Expected: True
##
##   Test Case 3:
##   Input: 19
##   Expected: True
##
##   Test Case 4:
##   Input: 8
##   Expected: False
##
##   Test Case 5:
##   Input: 7
##   Expected: True 
##   
##   Test Case 6:
##   Input: 5
##   Expected: False
##
##   Test Case 7:
##   Input: 25
##   Expected: False
##
##   Test Case 8:
##   Input: 0
##   Expected: False
##
"""
import unittest
# import pytest
from happy_number import is_happy_number

class TestHappyNumbers(unittest.TestCase):
    def test_case_1(self):
        input = 2147483646
        expected = False
        self.assertFalse(is_happy_number(input)[0])
    def test_case_2(self):
        input = 1
        expected = True
        self.assertTrue(is_happy_number(input)[0])
    def test_case_3(self):
        input = 19
        expected = True
        self.assertTrue(is_happy_number(input)[0])
    def test_case_4(self):
        input = 8
        expected = False
        self.assertFalse(is_happy_number(input)[0])
    def test_case_5(self):
        input = 7
        expected = True
        self.assertTrue(is_happy_number(input)[0])
    def test_case_6(self):
        input = 5
        expected = False
        self.assertFalse(is_happy_number(input)[0])
    def test_case_7(self):
        input = 25
        expected = False
        self.assertFalse(is_happy_number(input)[0])
    def test_case_8(self):
        input = 0
        expected = False
        self.assertFalse(is_happy_number(input)[0])
    def test_case_x(self):
        ...

if __name__ == '__main__':
    unittest.main(verbosity=2)
