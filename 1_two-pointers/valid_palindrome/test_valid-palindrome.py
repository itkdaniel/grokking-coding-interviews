# vim: set comments=sl\:\"\"\",m\:##\ \ \ \ ,ex-3\:\"\"\":
# vim: set fo=tcrq :
# vim: set comments=sb\:\"\"\",mb\:##\ \ \ \ ,ex-3\:\"\"\",\:##:
# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",\:##:
# vim: set fo=tcq1rowabvpn:

##  Valid Palindrome: Test Cases
import unittest
from valid_palindrome import ispalindrome
from palindrome_package.valid_palindrome_module import ispalindrome

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.str1 = 'kayak'
        self.str2 = 'hello'
        self.str3 = 'RACEACAR'
        self.str4 = 'A'
        self.str5 = 'ABCDABCD'
    def test_case_1(self):
        expected = True
        result = ispalindrome(self.str1)
        self.assertEqual(result, expected)
    def test_case_2(self):
        self.assertFalse(ispalindrome(self.str2))
    def test_case_3(self):
        self.assertFalse(ispalindrome(self.str3))
    def test_case_4(self):
        self.assertTrue(ispalindrome(self.str4))
    def test_case_5(self):
        self.assertFalse(ispalindrome(self.str5))

if __name__ == '__main__':
    unittest.main()
