# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   [('bbbbbb', 1), ('pwwkew', 3), ('', 0), ('conceptoftheday', 8), ('bbbbbbbbbbbbbbbb', 1), ('racecar', 4), ('bankrupted', 10), ('abcdbea', 5), ('aba', 2), ('abccabcabcc', 3), ('aaaabaaa', 2), ('bbbbb', 1)]
##
##   TestCase 1:
##   Input: 'bbbbbb'
##   Output: 1
##
##   TestCase 2:
##   Input: 'pwwkew'
##   Output: 3
##
##   TestCase 3:
##   Input: ''
##   Output: 0
##   ---------------------------------------------
##   TestCase 4:
##   Input: 'conceptoftheday'
##   Output: 8
##
##   TestCase 5:
##   Input: 'bbbbbbbbbbbbbbbb'
##   Output: 1
##
##   TestCase 6:
##   Input: 'racecar'
##   Output: 4
##
##   TestCase 7:
##   Input: 'bankrupted'
##   Output: 10
##   ---------------------------------------------
##   TestCase 8:
##   Input: 'abcdbea'
##   Output: 5
##
##   TestCase 9:
##   Input: 'aba'
##   Output: 2
##
##   TestCase 10:
##   Input: 'abccabcabcc'
##   Output: 3
##
##   TestCase 11:
##   Input: 'aaaabaaa'
##   Output: 2
##
##   TestCase 12:
##   Input: 'bbbbb'
##   Output: 1
##
"""
import unittest
from longest_substring_without_repeating_characters import find_longest_substring

class TestFindLongestSubstring(unittest.TestCase):
    def test_case_1(self):
        input = 'bbbbbb'
        expected = 1
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_2(self):
        input = 'pwwkew'
        expected = 3
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_3(self):
        input = ''
        expected = 0
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_4(self):
        input = 'conceptoftheday'
        expected = 8
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_5(self):
        input = 'bbbbbbbbbbbbbbbb'
        expected = 1
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_6(self):
        input = 'racecar'
        expected = 4
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_7(self):
        input = 'bankrupted'
        expected = 10
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_8(self):
        input = 'abcdbea'
        expected = 5
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_9(self):
        input = 'aba'
        expected = 2
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_10(self):
        input = 'abccabcabcc'
        expected = 3
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_11(self):
        input = 'aaaabaaa'
        expected = 2
        self.assertEqual(find_longest_substring(input),expected)
    def test_case_12(self):
        input = 'bbbbb'
        expected = 1
        self.assertEqual(find_longest_substring(input),expected)
