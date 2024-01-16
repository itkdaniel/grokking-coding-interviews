# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##   Test Case 1:
##   Input: k = 8, s = "AAAAACCCCCAAAAACCCCCC"
##   Output: set(["AAAAACCC", "AAAACCCC", "AAACCCCC"]) 
##
##   Test Case 2:
##   Input: k = 9, s = "GGGGGGGGGGGGGGGGGGGGGGGGG"
##   Output: set(["GGGGGGGGG"])
##
##   Test Case 3:
##   Input: k = 10, s = "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT"
##   Output: set(["TTTTTCCCCC","CCCCCTTTTT","TTTCCCCCCC","CCCCCCCTTT","TTCCCCCCCT","TCCCCCCCTT"])
##
##   Test Case 4:
##   Input: k = 10, s = "AAAAAACCCCCCCAAAAAAAACCCCCCCTG"
##   Output: set(["AAAAAACCCC", "AAAAACCCCC", "AAAACCCCCC", "AAACCCCCCC"])
##
##   Test Case 5:
##   Input: k = 6, s = "ATATATATATATATAT"
##   Output: set(["ATATAT","TATATA"])
##
"""
import unittest
from repeated_dna_sequences import find_repeated_sequences
from repeated_dna_sequences import find_repeated_sequences_polyroll_hashing

class TestRepeatedDNASequences(unittest.TestCase):
    def test_case_1(self):
        input = {"k":8,"s":"AAAAACCCCCAAAAACCCCCC"}
        expected = set(["AAAAACCC", "AAAACCCC", "AAACCCCC"])
        self.assertSetEqual(find_repeated_sequences(**input),expected)
    def test_case_2(self):
        input = {"k":9,"s":"GGGGGGGGGGGGGGGGGGGGGGGGG"}
        expected = set(["GGGGGGGGG"])
        self.assertSetEqual(find_repeated_sequences(**input),expected)
    def test_case_3(self):
        input = {"k":10,"s":"TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT"}
        expected = set(["CCCCCCCTTT", "CCCCCCTTTT", "CCCCCTTTTT", "CCCCTTTTTT", "TCCCCCCCTT", "TTCCCCCCCT", "TTTCCCCCCC", "TTTTCCCCCC", "TTTTTCCCCC"])
        self.assertSetEqual(find_repeated_sequences(**input),expected)
    def test_case_4(self):
        input = {"k":10,"s":"AAAAAACCCCCCCAAAAAAAACCCCCCCTG"}
        expected = set(["AAAAAACCCC", "AAAAACCCCC", "AAAACCCCCC", "AAACCCCCCC"])
        self.assertSetEqual(find_repeated_sequences(**input),expected)
    def test_case_5(self):
        input = {"k":6,"s":"ATATATATATATATAT"}
        expected = set(["ATATAT","TATATA"])
        self.assertSetEqual(find_repeated_sequences(**input),expected)

class TestRepeatedDNASequencesPolyRollHashing(unittest.TestCase):
    def test_case_1(self):
        input = {"k":8,"s":"AAAAACCCCCAAAAACCCCCC"}
        expected = set(["AAAAACCC", "AAAACCCC", "AAACCCCC"])
        self.assertSetEqual(find_repeated_sequences_polyroll_hashing(**input),expected)
    def test_case_2(self):
        input = {"k":9,"s":"GGGGGGGGGGGGGGGGGGGGGGGGG"}
        expected = set(["GGGGGGGGG"])
        self.assertSetEqual(find_repeated_sequences_polyroll_hashing(**input),expected)
    def test_case_3(self):
        input = {"k":10,"s":"TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT"}
        expected = set(["CCCCCCCTTT", "CCCCCCTTTT", "CCCCCTTTTT", "CCCCTTTTTT", "TCCCCCCCTT", "TTCCCCCCCT", "TTTCCCCCCC", "TTTTCCCCCC", "TTTTTCCCCC"])
        self.assertSetEqual(find_repeated_sequences_polyroll_hashing(**input),expected)
    def test_case_4(self):
        input = {"k":10,"s":"AAAAAACCCCCCCAAAAAAAACCCCCCCTG"}
        expected = set(["AAAAAACCCC", "AAAAACCCCC", "AAAACCCCCC", "AAACCCCCCC"])
        self.assertSetEqual(find_repeated_sequences_polyroll_hashing(**input),expected)
    def test_case_5(self):
        input = {"k":6,"s":"ATATATATATATATAT"}
        expected = set(["ATATAT","TATATA"])
        self.assertSetEqual(find_repeated_sequences_polyroll_hashing(**input),expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
