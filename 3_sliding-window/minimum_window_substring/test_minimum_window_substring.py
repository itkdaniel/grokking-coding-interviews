# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowpn:

##   Test Cases
"""
##    TestCase 1:
##    Input: s = "ABAACBBA", t = "ABC"
##                 s  e
##    {a:1,b:1,c:1},{a:1,b;1,c:1},fm=3
##    Output: "ACB"
##
##    TestCase 2:
##    Input: s = "ACBBACA", t = "ABA"
##    Output: "BACA"
##
##    TestCase 3:
##    Input: s = "ABAACBAB", t = "ABCC"
##    Output: ""
##
##    TestCase 4:
##    Input: s = "cabwefgewcwaefgcf", t = "cae"
##    Output: "cwae"
##   
##    TestCase 5:
##    Input: s = "bbaac", t = "aba"
##    {a:2,b:1},{b:1,a:2},fm=3
##    Output: "baa"
##   
##    TestCase 6:
##    Input: s = "AbabbbAbaA", t = "Bab"
##    Outut: ""
##
##    TestCase 7:
##    Input: s = "ABCD", t = "ABC"
##    Output: "ABC"
##
##    TestCase 8:
##    Input: s = "XYZYX", t = "XYZ"
##    Output: "XYZ"
##
##    TestCase 9:
##    Input: s = "ABXYZJKLSNFC", k = "ABC"
##    Output: "ABXYZJKLSNFC"
##
##    TestCase 10:
##    Input: s = "AAAAAAAAAAA", t = "A"
##    Output: "A"
##
##    TestCase 11:
##    Input: s = "ABDFGDCKAB", t = "ABCD"
##    Output: "DCKAB"
##    
##    inputs5 = [["cabwefgewcwaefgcf", "cae"],["ABAACBBA","ABC"],["AbabbbAbaA","Bab"],["bbaac","aba"],
##               ["ABAACBAB", "ABCC"],["ACBBACA", "ABA"],["ABDFGDCKAB","ABCD"],["AAAAAAAAAAA","A"],
##               ["ABXYZJKLSNFC","ABC"],["XYZYX","XYZ"],["ABCD","ABC"]]
##    [print(f'\x1b[0;35m{v+1}. \x1b[1;35m {inputs5[v]=},\n\x1b[1;34m minimum_window_substring(*inputs5[{v}])=',minimum_window_substring(*inputs5[v]),f'\x1b[0m') for v in range(len(inputs5))]
##
##    def find(*args):
##        pargs = ''.join(args) if args else ''
##        return subprocess.check_output(['find','/home/danyosaan/','-name',pargs]).decode().strip('\n')
##    def vim(*args):
##        pargs = ''.join(args) if args else ''
##        file = find(pargs) 
##        os.system(f'vim {file if file else ""}')
##    def cat(*args):
##        pargs = ''.join(args) if args else ''
##        file = find(pargs)
##        content = subprocess.check_output(['cat',file]).decode()
##        print(content)
##    def run(*args):
##        pargs = ''.join(args) if args else ''
##        os.system(pargs)
##    def exec_tests(*args):
##        pargs = ''.join(args) if args else ''
##        test_file_path = find(pargs) if pargs.startswith('test_') and pargs.endswith('.py')) else find('test_'+pargs)
##        test_file = test_file_path.split('/')[-1] if test_file_path else ''
##        exec_string = f'cd {test_file_path.split('/')[-2]} ; python3 -m unittest {test_file}'
##        
##        print('\x1b[1;35m Executing File:\x1b[1;34m {test_file}\x1b[0m')
##        print('\x1b[1;35m Full Path:\x1b[1;34m {test_file_path}\x1b[0m')
##        print('\x1b[0;33m')
##        # subprocess.check_output(['python3','-m','unittest',test_file_path])
##        os.system(exec_string)
##        print('\x1b[0m')
"""
import unittest
from minimum_window_substring import minimum_window_substring
from minimum_window_substring import minimum_window_substring2

class TestMinimumWindowSubString(unittest.TestCase):
    def test_case_1(self):
        inputs = ["cabwefgewcwaefgcf", "cae"]
        expected = "cwae"
        self.assertEqual(minimum_window_substring(*inputs),expected)
    def test_case_2(self):
        inputs = ["ABAACBBA","ABC"]
        expected = "ACB"
        self.assertEqual(minimum_window_substring(*inputs),expected)
    def test_case_3(self):
        inputs = ["AbabbbAbaA","Bab"]
        expected = ""
        self.assertEqual(minimum_window_substring(*inputs),expected)
    def test_case_4(self):
        inputs = ["bbaac","aba"]
        expected = "baa"
        self.assertEqual(minimum_window_substring(*inputs),expected)
    def test_case_5(self):
        inputs =  ["ABCD","ABC"]
        expected = "ABC"
        self.assertEqual(minimum_window_substring(*inputs),expected)

class TestMinimumWindowSubString2(unittest.TestCase):
    def test_case_1(self):
        inputs = ["ACBBACA", "ABA"]
        expected = "BACA"
        self.assertEqual(minimum_window_substring2(*inputs),expected)
    def test_case_2(self):
        inputs = ["ABDFGDCKAB","ABCD"]
        expected = "DCKAB"
        self.assertEqual(minimum_window_substring2(*inputs),expected)
    def test_case_3(self):
        inputs = ["AAAAAAAAAAA","A"]
        expected = "A"
        self.assertEqual(minimum_window_substring2(*inputs),expected)
    def test_case_4(self):
        inputs = ["ABXYZJKLSNFC","ABC"]
        expected = "ABXYZJKLSNFC"
        self.assertEqual(minimum_window_substring2(*inputs),expected)
    def test_case_5(self):
        inputs = ["XYZYX","XYZ"]
        expected = "XYZ"
        self.assertEqual(minimum_window_substring2(*inputs),expected)
    def test_case_6(self):
        inputs = ["ABAACBAB", "ABCC"]
        expected = ""
        self.assertEqual(minimum_window_substring2(*inputs),expected)


if __name__ == '__main__':
#    unittest.main(verbosity=2)
    suite1 = unittest.TestSuite()
    suite2 = unittest.TestSuite()
    
    suite1.addTest(TestMinimumWindowSubString)
    suite2.addTest(TestMinimumWindowSubString2)

    runner = unittest.TextTestRunner(verbosity=2)

    runner.run()

