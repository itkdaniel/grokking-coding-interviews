# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

import unittest
from sort_colors import sort_colors
##   Test Cases
"""
##   TestCase 1: Input: [0, 1, 0],
##               Expected: [0, 0, 1]
##   TestCase 2: Input: [1, 1, 0, 2],
##               Expected: [0, 1, 1, 2]
##   TestCase 3: Input: [2, 1, 1, 0, 0],
##               Expected: [0, 0, 1, 1, 2]
##   TestCase 4: Input: [2, 2, 2, 0, 1, 0],
##               Expected: [0, 0, 1, 2, 2, 2]
##   TestCase 5: Input: [2, 1, 1, 0, 1, 0, 2],
##               Expected: [0, 0, 1, 1, 1, 2, 2]
##
"""
class TestSortColors(unittest.TestCase):
    def test_case_1(self):
        input = [0,1,0]
        expected = [0,0,1]
        return self.assertListEqual(sort_colors(input), expected)
    def test_case_2(self):
        input = [1,1,0,2]
        expected = [0,1,1,2]
        return self.assertListEqual(sort_colors(input), expected)
    def test_case_3(self):
        input = [2,1,1,0,0]
        expected = [0,0,1,1,2]
        return self.assertListEqual(sort_colors(input), expected)
    def test_case_4(self):
        input = [2,2,2,0,1,0]
        expected = [0,0,1,2,2,2]
        return self.assertListEqual(sort_colors(input), expected)
    def test_case_5(self):
        input = [2,1,1,0,1,0,2]
        expected = [0,0,1,1,1,2,2]
        return self.assertListEqual(sort_colors(input), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
