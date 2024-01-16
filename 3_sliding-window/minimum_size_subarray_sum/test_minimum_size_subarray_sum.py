# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   TestCase 1:
##   inputs: ([2, 3, 1, 2, 4, 3], 7)
##   output: ([[4, 3], 3], 2)
##
##   TestCase 2:
##   input: ([1, 1, 1, 1, 1, 3], 11)
##   output: ([[], 8], 0)
##
##   TestCase 3:
##   input: [[1, 2, 7, 3, 4, 5], 10]
##   output: ([[3, 4, 5], 9], 2)
##   
##   TestCase 4:
##   input: [[7, 2, 4, 6, 5, 8], 6]
##   output: ([[8], 0], 1)
##
##   TestCase 5:
##   input: [[1, 3, 4, 5, 2], 12]
##   output: ([[3, 4, 5], 11], 3)
##
##   TestCase 6:
##   input: [[7, 2, 4, 6, 5, 8], 6]
##   output: ([[8], 0], 1)
##
##   TestCase 7:
##   input: [[2, 3, 1, 2, 4, 3], 7]
##   output: ([[4, 3], 3], 2)
##
##   TestCase 8:
##   input: [[1, 4, 4], 4]
##   output: ([[4], 0], 1)
##
##   TestCase 9:
##   input: [[1, 1, 1, 1, 1, 1, 1, 1], 11]
##   output: ([[], 8], 0)
##
##   TestCase 10:
##   input: [[1, 2, 3, 4], 10]
##   output: ([[1, 2, 3, 4], 9], 4)
##   
##   TestCase 11:
##   input: [[1, 2, 1, 3], 5]
##   output: ([[2, 1, 3], 4], 3)
##   
input: [[2, 3, 1, 2, 4, 3], 7]
   output: ([[4, 3], 3], 2)
input: [[1, 1, 1, 1, 1, 3], 11]
   output: ([[], 8], 0)
input: [[1, 2, 7, 3, 4, 5], 10]
   output: ([[3, 4, 5], 9], 2)
input: [[7, 2, 4, 6, 5, 8], 6]
   output: ([[8], 0], 1)
input: [[1, 3, 4, 5, 2], 12]
   output: ([[3, 4, 5], 11], 3)
input: [[7, 2, 4, 6, 5, 8], 6]
   output: ([[8], 0], 1)
input: [[2, 3, 1, 2, 4, 3], 7]
   output: ([[4, 3], 3], 2)
input: [[1, 4, 4], 4]
   output: ([[4], 0], 1)
input: [[1, 1, 1, 1, 1, 1, 1, 1], 11]
   output: ([[], 8], 0)
input: [[1, 2, 3, 4], 10]
   output: ([[1, 2, 3, 4], 9], 4)
input: [[1, 2, 1, 3], 5]
   output: ([[2, 1, 3], 4], 3)
"""
import unittest
from minimum_size_subarray_sum import min_subarray_len

class TestMinimumSizeSubarrayLength(unittest.TestCase):
    def test_case_1(self):
        inputs = ([2, 3, 1, 2, 4, 3], 7)
        expected = 2
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_2(self):
        inputs = ([1, 1, 1, 1, 1, 3], 11)
        expected = 0
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_4(self):
        inputs = ([1, 2, 7, 3, 4, 5], 10)
        expected = 2
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_5(self):
        inputs = ([7, 2, 4, 6, 5, 8], 6)
        expected = 1
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_6(self):
        inputs = ([1, 3, 4, 5, 2], 12)
        expected = 3
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_7(self):
        inputs = ([7, 2, 4, 6, 5, 8], 6)
        expected = 1
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_8(self):
        inputs = ([2, 3, 1, 2, 4, 3], 7)
        expected = 2
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_9(self):
        inputs = ([1, 4, 4], 4)
        expected = 1
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_10(self):
        inputs = ([1, 1, 1, 1, 1, 1, 1, 1], 11)
        expected = 0
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_11(self):
        inputs = ([1, 2, 3, 4], 10)
        expected = 4
        self.assertEqual(min_subarray_len(*inputs),expected)
    def test_case_12(self):
        inputs = ([1, 2, 1, 3], 5)
        expected = 3
        self.assertEqual(min_subarray_len(*inputs),expected)

if __name__ == '__main__':
    unittest.main()
