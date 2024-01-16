# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   TestCase 1:
##   Input: nums = [1,2,3,4,5,6,7,8,9,10], w = 3
##   Output: [3,4,5,6,7,8,9,10]
##
##   TestCase 2:
##   Input: nums = [3,3,3,3,3,3,3,3,3,3], w = 4
##   Output: [3,3,3,3,3,3,3]
##
##   TestCase 3:
##   Input: nums = [10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67], w = 3
##   Output: [10,9,23,23,34,56,67,67,67,-1,-2,9,10,34,67]
##
##   TestCase 4:
##   Input: nums = [4,5,6,1,2,3], w = 1
##   Output: [4,5,6,1,2,3]
##
##   TestCase 5:
##   Input: nums = [9,5,3,1,6,3], w = 2
##   Output: [9,5,3,6,6]
##
"""
import unittest
from maximum_in_sliding_window import find_max_sliding_window
class TestMaximumInSlidingWindow(unittest.TestCase):
    def test_case_1(self):
        inputs = {'nums':[1,2,3,4,5,6,7,8,9,10],'w':3}
        expected = [3,4,5,6,7,8,9,10]
        self.assertListEqual(find_max_sliding_window(**inputs),expected)
    def test_case_2(self):
        inputs = {'nums':[3,3,3,3,3,3,3,3,3,3],'w':4}
        expected = [3,3,3,3,3,3,3]
        self.assertListEqual(find_max_sliding_window(**inputs),expected)
    def test_case_3(self):
        inputs = {'nums':[10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67],'w':3}
        expected = [10,9,23,23,34,56,67,67,67,-1,-2,9,10,34,67]
        self.assertListEqual(find_max_sliding_window(**inputs),expected)
    def test_case_4(self):
        inputs = {'nums':[4,5,6,1,2,3],'w':1}
        expected = [4,5,6,1,2,3]
        self.assertListEqual(find_max_sliding_window(**inputs),expected)
    def test_case_5(self):
        inputs = {'nums':[9,5,3,1,6,3],'w':2}
        expected = [9,5,3,6,6]
        self.assertListEqual(find_max_sliding_window(**inputs),expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
