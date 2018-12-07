import unittest
from factorial import main

class TestFactorial(unittest.TestCase):
    def test_fact(self):
        exp_result=5
        main.x=3
        test_result=main()
        self.assertEqual(exp_result,test_result)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
