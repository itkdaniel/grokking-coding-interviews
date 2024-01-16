# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

import unittest
#import pytest

from reverse_words_in_sentence import reverse_sentence

##   Test Cases
"""
##   TestCase 1:
##   Input: "Hello Friend"
##   Expected: "Friend Hello"
##
##   Test Case 2:
##   Input: "    We love Python"
##   Expected: "Python love We"
##
##   Test Case 3:
##   Input: "The quick brown fox jumped over the lazy dog   "
##   Expected: "dog lazy the over jumped fox brown quick The"
##
##   Test Case 4:
##   Input: "Hey"
##   Expected: "Hey"
##
##   Test Case 5:
##   Input: "To be or not to be"
##   Expected: "be to not or be To"
##
##   Test Case 6:
##   Input: "AAAAA"
##   Expected: "AAAAA"
##
##   Test Case 7:
##   Input: "Hello     World"
##   Expected: "World Hello"
##
"""

class TestReverseWordsInString(unittest.TestCase):
    def test_case_1(self):
        input = "Hello Friend"
        expected = "Friend Hello"
        return self.assertEqual(reverse_sentence(input), expected)

    def test_case_2(self):
        input = "    We love Python"
        expected = "Python love We"
        return self.assertEqual(reverse_sentence(input), expected)

    def test_case_3(self):
        input = "The quick brown fox jumped over the lazy dog   "
        expected = "dog lazy the over jumped fox brown quick The"
        return self.assertEqual(reverse_sentence(input), expected)

    def test_case_4(self):
        input = "Hey"
        expected = "Hey"
        return self.assertEqual(reverse_sentence(input), expected)

    def test_case_5(self):
        input = "To be or not to be"
        expected = "be to not or be To"
        return self.assertEqual(reverse_sentence(input), expected)

    def test_case_6(self):
        input = "AAAAA"
        expected = "AAAAA"
        return self.assertEqual(reverse_sentence(input), expected)

    def test_case_7(self):
        input = "Hello     World"
        expected = "World Hello"

if __name__ == '__main__':
    unittest.main(verbosity=2)
