# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   TestCase 1:
##   Input: prices = [7, 1, 5, 3, 6, 4]
##   Output: 5
##
##   TestCase 2:
##   Input: [10, 8, 6, 4, 2]
##   Output: 0
##
##   TestCase 3:
##   Input: [10, 4, 11, 1, 5]
##   Output: 7
##
##   TestCase 4:
##   Input: [7, 7, 6, 6, 6]
##   Output: 0
##
##   TestCase 5:
##   Input: [4, 10, 5, 1, 6, 7]
##   Output: 6
##
##   TestCase 6:
##   Input: [4, 4, 4, 3, 3, 4]
##   Output: 1
##
##   TestCase 7:
##   Input: [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
##   Output: 9
##
##   TestCase 8:
##   Input: [7, 1, 5, 3, 6, 4]
##   Output: 5
##
##   TestCase 9:
##   Input: [7, 6, 4, 3, 1]
##   Output: 0
##
##   TestCase 10:
##   Input: [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]
##   Output: 7
##
##   TestCase 11:
##   Input: [1, 4, 2]
##   Output: 3
##
"""
import unittest
from best_time_buy_sell_stock import max_profit

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_case_1(self):
        inputs = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_2(self):
        inputs = [10, 8, 6, 4, 2]
        expected = 0
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_3(self):
        inputs = [10, 4, 11, 1, 5]
        expected = 7
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_4(self):
        inputs = [7, 7, 6, 6, 6]
        expected = 0
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_5(self):
        inputs = [4, 10, 5, 1, 6, 7]
        expected = 6
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_6(self):
        inputs = [4, 4, 4, 3, 3, 4]
        expected = 1
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_7(self):
        inputs = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
        expected = 9
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_8(self):
        inputs = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_9(self):
        inputs = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_10(self):
        inputs = [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]
        expected = 7
        self.assertEqual(max_profit(inputs)[1],expected)
    def test_case_11(self):
        inputs = [1, 4, 2]
        expected = 3
        self.assertEqual(max_profit(inputs)[1],expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
