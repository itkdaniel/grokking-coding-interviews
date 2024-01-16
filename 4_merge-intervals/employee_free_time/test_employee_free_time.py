# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   TestCase 1:
##   inputs = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
##   expected = [[3,4]]
##
##   TestCase 2:
##   inputs = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
##   expected = [[5,6],[7,9]]
##
##   TestCase 3:
##   inputs = [[[2,3],[7,9]],[[1,4],[6,7]]]
##   expected = [[4,6]]
##   
##   TestCase 4:
##   inputss = [[[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]]]
##   expected = [[6,8]]
##
##   TestCase 5:
##   inputs = [[[1, 3], [5, 6], [9, 10]],[[2, 4], [7, 8]], [[8, 11], [12, 14]]]
##   expected = [[4, 5], [6, 7], [11, 12]]
##
##   TestCase 6:
##   inputs = [[[1, 2], [3, 4]], [[2, 3]], [[4, 6]]]
##   expected = [[3,4]]
##
##   TestCase 7:
##   inputs = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
##   expected =   
##
##   TestCase 8:
##   inputs = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
##   expected = [[5,6],[7,9]]
##
##   TestCase 9:
##   inputs = [[[2,3],[7,9]],[[1,4],[6,7]]]
##   expected = [[4,6]]
##
##   TestCase 10:
##   inputs = [[[3,5],[8,10]],[[4,6],[9,12]],[[5,6],[8,10]]]
##   expected = [[6,8]]
##
##   TestCase 11:
##   inputs = [[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]]
##   expected = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]
##
"""
import unittest
from employee_free_time import employee_free_time

class TestEmployeeFreeTime(unittest.TestCase):
    def test_case_1(self):
        inputs = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
        expected = [[3,4]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_2(self):
        inputs = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
        expected = [[5,6],[7,9]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_3(self):
        inputs = [[[2,3],[7,9]],[[1,4],[6,7]]]
        expected = [[4,6]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_4(self):
        inputs = [[[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]]]
        expected = [[6,8]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_5(self):
        inputs = [[[1, 3], [5, 6], [9, 10]],[[2, 4], [7, 8]], [[8, 11], [12, 14]]]
        expected = [[4, 5], [6, 7], [11, 12]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_6(self):
        inputs = [[[1, 2], [3, 4]], [[2, 3]], [[4, 6]]]
        expected = []
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_7(self):
        inputs = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
        expected = [[3, 4]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_8(self):
        inputs = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
        expected = [[5, 6], [7, 9]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_9(self):
        inputs = [[[2,3],[7,9]],[[1,4],[6,7]]]
        expected = [[4, 6]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_10(self):
        inputs = [[[3,5],[8,10]],[[4,6],[9,12]],[[5,6],[8,10]]]
        expected = [[6, 8]]
        self.assertListEqual(employee_free_time(inputs),expected)
    def test_case_11(self):
        inputs = [[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]]
        expected = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]
        self.assertListEqual(employee_free_time(inputs),expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
