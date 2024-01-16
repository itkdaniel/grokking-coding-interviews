# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   
##   TestCase 1:
##   Input: [[1,3],[2,6],[8,10],[15,18],[18,20]]
##   Output: [[1,6],[8,10],[15,20]]
##
##   TestCase 2:
##   Input: [[10,12],[12,15]]
##   Output: [[10,15]]
##
##   TestCase 3:
##   Input: [[1,5],[3,7],[4,6],[6,8]]
##   Output: [[1,8]]
##
##   TestCase 4:
##   Input: [[2,4],[3,5],[4,5],[6,10],[12,14]]
##   Output: [[2,5],[6,10],[12,14]]
##
##   TestCase 5:
##   Input: [[2,9],[3,5],[4,8]]
##   Output: [[2,9]]
##
##   TestCase 6:
##   Input: [[1,8]]
##   Output:[[1,8]]
##
##   TestCase 7:
##   Input: [[1,6],[2,4]]
##   Output: [[1,6]]
##
##   TestCase 8:
##   Input: [[1,5],[3,7],[4,6]]
##   Output: [[1,7]]
##
##   TestCase 9:
##   Input: [[1,5],[4,6],[6,8],[11,15]]
##   Output: [[1,8],[11,15]]
##
##   TestCase 10:
##   Input: [[1,5]]
##   Output: [[1,5]]
##
##   TestCase 11:
##   Input: [[1,9],[3,8],[4,4]]
##   Output: [[1,9]]
##
##   TestCase 12:
##   Input: [[1,2],[3,4],[8,8]]
##   Output: [[1,2],[3,4],[8,8]]
##   
##   TestCase 13:
##   Input: [[1, 5], [3, 7], [4, 6]],
##   Output: [[1,7]]]
##   
##   TestCase 14:
##   Input: [[1, 5], [4, 6], [6, 8], [11, 15]]
##   Output: [[1,8],[11,15]]
##   
##   TestCase 15:
##   Input: [[3, 7], [6, 8], [10, 12], [11, 15]],
##   Outut: [[3,8],[10,15]]
##   
##   TestCase 16:
##   Input: [[1, 5]],
##   Output: [[1,5]]
##
##   TestCase 17:
##   Input: [[1, 9], [3, 8], [4, 4]],
##   Output: [[1,9]]
##
##   TestCase 18:
##   Input: [[1, 5], [1, 3]],
##   Output: [[1,5]]   
##   
##   TestCase 19:
##   Input: [[1, 5], [6, 9]],
##   Output: [[1,5],[6,9]]
##   
##   TestCase 20:
##   Input: [[0, 0], [1, 18], [1, 3]]
##   Output: [[0,0],[1,18]]
"""
import unittest
from merged_intervals import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_case_1(self):
        inputs = [[2,9],[3,5],[4,8]]
        expected = [[2,9]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_2(self):
        inputs = [[10,12],[12,15]]
        expected = [[10,15]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_3(self):
        inputs = [[1,5],[3,7],[4,6],[6,8]] 
        expected = [[1,8]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_4(self):
        inputs = [[2,4],[3,5],[4,5],[6,10],[12,14]] 
        expected = [[2,5],[6,10],[12,14]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_5(self):
        inputs = [[2,9],[3,5],[4,8]] 
        expected = [[2,9]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_6(self):
        inputs = [[1,8]] 
        expected = [[1,8]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_7(self):
        inputs = [[1,6],[2,4]]
        expected = [[1,6]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_8(self):
        inputs = [[1,5],[3,7],[4,6]] 
        expected = [[1,7]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_9(self):
        inputs = [[1,5],[4,6],[6,8],[11,15]] 
        expected = [[1,8],[11,15]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_10(self):
        inputs = [[1,5]] 
        expected = [[1,5]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_11(self):
        inputs = [[1,9],[3,8],[4,4]]
        expected = [[1,9]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_12(self):
        inputs = [[1,2],[3,4],[8,8]] 
        expected = [[1,2],[3,4],[8,8]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_13(self):
        inputs = [[1, 5], [3, 7], [4, 6]] 
        expected = [[1,7]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_14(self):
        inputs = [[1, 5], [4, 6], [6, 8], [11, 15]] 
        expected = [[1,8],[11,15]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_15(self):
        inputs = [[3, 7], [6, 8], [10, 12], [11, 15]] 
        expected = [[3,8],[10,15]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_16(self):
        inputs = [[1, 9], [3, 8], [4, 4]] 
        expected = [[1,9]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_17(self):
        inputs = [[1, 5], [1, 3]] 
        expected = [[1,5]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_18(self):
        inputs = [[1, 5], [6, 9]] 
        expected = [[1,5],[6,9]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_19(self):
        inputs = [[0, 0], [1, 18], [1, 3]]
        expected = [[0,0],[1,18]]
        self.assertListEqual(merge_intervals(inputs),expected)
    def test_case_20(self):
        inputs = [[1,5],[2,3],[4,8],[9,11],[12,13]]
        expected = [[1,8],[9,11],[12,13]]
        self.assertListEqual(merge_intervals(inputs),expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
