# vim: set comments=sl\:\"\"\",m\:##\ \ \ \ ,ex-3\:\"\"\":
# vim: set fo=tcrq :
# vim: set comments=sb\:\"\"\",mb\:##\ \ \ \ ,ex-3\:\"\"\",\:##:
# vim: set fo=tcq1rowabvpn:

##   Test Cases
import unittest
from sum_of_three_values import find_sum_of_three

class TestSumOfThreeNums(unittest.TestCase):
    def test_case_1(self):
        input = ([1,-1,0], -1)
        self.assertFalse(find_sum_of_three(*input))
    def test_case_2(self):
        input = ([3,7,1,2,8,4,5], 10)
        self.assertTrue(find_sum_of_three(*input))
    def test_case_3(self):
        input = ([3,7,1,2,8,4,5], 21)
        self.assertFalse(find_sum_of_three(*input))
    def test_case_4(self):
        input = ([-1,2,1,-4,5,-3], -8)
        self.assertTrue(find_sum_of_three(*input))
    def test_case_5(self):
        input = ([-1,2,1,-4,5,-3], 0)
        self.assertTrue(find_sum_of_three(*input))
    def test_case_6(self):
        input = ([8,2,4,9,5], 17)
        self.assertTrue(find_sum_of_three(*input))
if __name__ == '__main__':
    unittest.main(verbosity=2)
