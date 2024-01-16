# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

##   Test Cases
"""
##   Test Case 1:
##   Input: "madame"
##   Output: True
##
##   Test Case 2:
##   Input: "dead"
##   Output: True
##
##   Test Case 3:
##   Input: "abca"
##   Output: True
##
##   Test Case 4:
##   Input: "tebbem"
##   Output: False
##
##   Test Case 5:
##   Input: "eeccccbebaeeabebccceea"
##   Output: True
##
"""

import unittest
#import pytest
from valid_palindrome_ii import is_palindrome

class TestValidPalindromeII(unittest.TestCase):
    def test_case_1(self):
        input = "madame"
        expected = True
        return self.assertTrue(is_palindrome(input))
    def test_case_2(self):
        input = "dead"
        expected = True
        return self.assertTrue(is_palindrome(input))
    def test_case_3(self):
        input = "abca"
        expected = True
        return self.assertTrue(is_palindrome(input))
    def test_case_4(self):
        input = "tebbem"
        expected = False
        return self.assertFalse(is_palindrome(input))
    def test_case_5(self):
        input = "eeccccbebaeeabebccceea"
        expected = False
        return self.assertFalse(is_palindrome(input))

if __name__ == '__main__':
    unittest.main(verbosity=2)
