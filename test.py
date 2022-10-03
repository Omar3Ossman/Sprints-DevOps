import unittest

target = __import__("sprints")

"""
0- zeros
1- float and integers mixed
2- floats only
3- integers only 
4- negative numbers
5- strings
6- empty input
"""
class TestSum(unittest.TestCase):
    
    def testCase0(self):
        print("TEST CASE 0: zeros")
        data = "0 0 0"
        result = target.myFunc(data)
        self.assertEqual(result, (0.0, 0.0), "Should be zeros")
        print()
    def testCase1(self):
        print("TEST CASE 1: float and integers mixed")
        data = "1 0.5 -2 1.99 -.35 2.0 99 -99 2 4 6"
        result = target.myFunc(data)
        self.assertEqual(result, (2.5, 2.0), "Should be 2 and 2.0")
        print()
    
    def testCase2(self):
        print("TEST CASE 2: floats only")
        data = "0.5 1.99 -.35 -2.0"
        result = target.myFunc(data)
        self.assertEqual(result, (0.0, 1.99), "Should be 0 and 1.99")
        print()

    def testCase3(self):
        print("TEST CASE 3: integers only ")
        data = "1 -2 2 99 -99 2 4 6"
        result = target.myFunc(data)
        self.assertEqual(result, (2.4, 0.0), "Should be 2 and 0")
        print()
    
 

if __name__ == '__main__':
    unittest.main()   
    