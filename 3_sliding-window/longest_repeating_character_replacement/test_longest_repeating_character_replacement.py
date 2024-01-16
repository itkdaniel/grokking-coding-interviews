# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   TestCase 1:
##   Input: s = "aaacbbbaabab", k = 2
##   Output: 6
##
##   TestCase 2:
##   Input: s = "aaacbbbaabab", k = 1
##   Output: 4
##
##   TestCase 3:
##   Input: s = "dippitydip", k = 4
##   Output: 6
##
##   TestCase 4:
##   Input: s = "coollooc", k = 2
##   Output: 6
##
##   TestCase 5:
##   Input: s = "aaaaaaaaaa", k = 2
##   Output: 10
##
"""
import unittest
from longest_repeating_character_replacement import longest_repeating_character_replacements
from longest_repeating_character_replacement import longest_repeating_character_replacements2

class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def test_case_1(self):
        inputs = ["aaacbbbaabab", 2]
        expected = 6
        self.assertEqual(longest_repeating_character_replacements(*inputs),expected)
    def test_case_2(self):
        inputs = ["aaacbbbaabab", 1]
        expected = 4
        self.assertEqual(longest_repeating_character_replacements(*inputs),expected)
    def test_case_3(self):
        inputs = ["dippitydip", 4]
        expected = 6
        self.assertEqual(longest_repeating_character_replacements(*inputs),expected)
    def test_case_4(self):
        inputs = ["coollooc", 2]
        expected = 6
        self.assertEqual(longest_repeating_character_replacements(*inputs),expected)
    def test_case_5(self):
        inputs = ["aaaaaaaaaa", 2]
        expected = 10
        self.assertEqual(longest_repeating_character_replacements(*inputs),expected)

class TestLongestRepeatingCharacterReplacement2(unittest.TestCase):
    def test_case_6(self):
        inputs = ["aaacbbbaabab", 2]
        expected = 6
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_7(self):
        inputs = ["aaacbbbaabab", 1]
        expected = 4
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_8(self):
        inputs = ["dippitydip", 4]
        expected = 6
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_9(self):
        inputs = ["coollooc", 2]
        expected = 6
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_10(self):
        inputs = ["aaaaaaaaaa", 2]
        expected = 10
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    """
    ##   More Test Cases
    ##   str_inputs = ["aabccbb", "abbcb", "abccde", "abbcab", "bbbbbbbbb"]
    ##   k_inputs = [2, 1, 1, 2, 4]
    ##   
    """
    def test_case_11(self):
        inputs = ["aabccbb",2]
        expected = 5
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_12(self):
        inputs = ["abbcb",1]
        expected = 4
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_13(self):
        inputs = ["abccde",1]
        expected = 3
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_14(self):
        inputs = ["abbcab",2]
        expected = 5
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)
    def test_case_15(self):
        inputs = ["bbbbbbbbb",4]
        expected = 9
        self.assertEqual(longest_repeating_character_replacements2(*inputs),expected)

class TestCaseRunner(unittest.TextTestRunner,unittest.TestSuite):
    def __init__(self):
        self.suite1 = self.TestSuite()
        self.suite2 = self.TestSuite()

if __name__ == '__main__':
    #unittest.main(verbosity=2)
    
    suite1 = unittest.TestSuite()
    suite2 = unittest.TestSuite()
    
    for i in range(1,6):
        suite1.addTest(TestLongestRepeatingCharacterReplacement(f'test_case_{i}'))
    for i in range(6,16):
        suite2.addTest(TestLongestRepeatingCharacterReplacement2(f'test_case_{i}'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite1)
    runner.run(suite2)
