# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   TestCase 1:
##   inputs: [[[1, 4], [5, 6], [7, 9]], [[3, 5], [6, 7], [8, 9]]]
##   output: [[3, 4], [5, 5], [6, 6], [7, 7], [8, 9]]
##
##   TestCase 2:
##   inputs: [[[0, 4], [5, 7], [8, 12], [13, 15], [16, 18]], [[0, 18]]]
##   output: [[0, 4], [5, 7], [8, 12], [13, 15], [16, 18]]
##
##   TestCase 3:
##   inputs: [[[2, 6], [7, 9], [10, 13], [14, 19], [20, 24]], [[1, 4], [6, 8], [15, 18]]]
##   output: [[2, 4], [6, 6], [7, 8], [15, 18]]
##
##   TestCase 4:
##   inputs: [[[1, 29]], [[1, 5], [6, 10], [11, 14], [15, 18], [19, 20]]]
##   output: [[1, 5], [6, 10], [11, 14], [15, 18], [19, 20]]
##
##   TestCase 5:
##   inputs: [[[1, 4], [5, 6], [7, 8], [9, 15]], [[2, 4], [5, 7], [9, 15]]]
##   output: [[2, 4], [5, 6], [7, 7], [9, 15]]
##
##   TestCase 6:
##   inputs: [[[1, 3], [4, 6], [8, 10], [11, 15]], [[2, 3], [10, 15]]]
##   output: [[2, 3], [10, 10], [11, 15]]
##
##   TestCase 7:
##   inputs: [[[1, 2], [4, 6], [7, 8], [9, 10]], [[3, 6], [7, 8], [9, 10]]]
##   output: [[4, 6], [7, 8], [9, 10]]
##
##   TestCase 8:
##   inputs: [[[1, 3], [5, 6], [7, 8], [9, 10], [12, 15]], [[2, 4], [7, 10]]]
##   output: [[2, 3], [7, 8], [9, 10]]
##
##   TestCase 9:
##   inputs: [[[1, 2]], [[1, 2]]]
##   output: [[1, 2]]
##   
"""
import unittest
from interval_list_intersections import intervals_intersection

class TestIntervalListIntersections(unittest.TestCase):
    def test_case_1(self):
        inputs = [[[1, 4], [5, 6], [7, 9]], [[3, 5], [6, 7], [8, 9]]]
        expected = [[3, 4], [5, 5], [6, 6], [7, 7], [8, 9]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_2(self):
        inputs = [[[0, 4], [5, 7], [8, 12], [13, 15], [16, 18]], [[0, 18]]]
        expected = [[0, 4], [5, 7], [8, 12], [13, 15], [16, 18]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_3(self):
        inputs = [[[2, 6], [7, 9], [10, 13], [14, 19], [20, 24]], [[1, 4], [6, 8], [15, 18]]]
        expected = [[2, 4], [6, 6], [7, 8], [15, 18]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_4(self):
        inputs = [[[1, 29]], [[1, 5], [6, 10], [11, 14], [15, 18], [19, 20]]]
        expected = [[1, 5], [6, 10], [11, 14], [15, 18], [19, 20]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_5(self):
        inputs = [[[1, 4], [5, 6], [7, 8], [9, 15]], [[2, 4], [5, 7], [9, 15]]]
        expected = [[2, 4], [5, 6], [7, 7], [9, 15]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_6(self):
        inputs = [[[1, 3], [4, 6], [8, 10], [11, 15]], [[2, 3], [10, 15]]]
        expected = [[2, 3], [10, 10], [11, 15]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_7(self):
        inputs = [[[1, 2], [4, 6], [7, 8], [9, 10]], [[3, 6], [7, 8], [9, 10]]]
        expected = [[4, 6], [7, 8], [9, 10]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_8(self):
        inputs = [[[1, 3], [5, 6], [7, 8], [9, 10], [12, 15]], [[2, 4], [7, 10]]]
        expected = [[2, 3], [7, 8], [9, 10]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_9(self):
        inputs = [[[1, 2]], [[1, 2]]]
        expected = [[1, 2]]
        self.assertListEqual(intervals_intersection(*inputs),expected)
    """
    def test_case_x(self):
        inputs = []
        expected = 0
        self.assertListEqual(intervals_intersection(*inputs),expected)
    def test_case_x(self):
        inputs = []
        expected = 0
        sself.assertListEqual(intervals_intersection(*inputs),expected)
    """
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
