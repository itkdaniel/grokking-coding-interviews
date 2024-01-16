# vim: set comments=sb\:\"\"\",mb\:\ \ \ ,ex-3\:\"\"\",\:##:
# vim: set fo=tcq1rowabvpn:

##   Test Cases
import unittest

class TestRemoveNthFromEndList(unittest.TestCase):
    def test_case_1(self):
        lst = [23, 89, 10, 5, 67, 39, 70, 28]
        n = 4
        expected = [23, 89, 10, 5, 39, 70, 28]
    def test_case_2(self):
        lst = [34, 53, 6, 95, 38, 28, 17, 63, 16, 76]
        n = 1
        expected = [34, 53, 6, 95, 38, 28, 17, 63, 16]
    def test_case_3(self):
        lst = [288, 224, 275, 390, 4, 383, 330, 60, 193]
        n = 6
        expected = [288, 224, 275, 4, 383, 330, 60, 193]
    def test_case_4(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = 9
        expected = [2, 3, 4, 5, 6, 7, 8, 9]
    def test_case_5(self):
        lst = [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]
        n = 11
        expected = [69, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]

if __name__ == '__main__':
    unittest.main(verbosity=2)
