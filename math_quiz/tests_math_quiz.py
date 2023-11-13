import unittest
from math_quiz import random_int, random_choice, fun_operator
import random

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        random.seed(76)
        for _ in range(1000):
            op = random_choice()
            self.assertIn(op, ['+', '-', '*'])

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 4, '-', '4 - 4', 0),
                (5, 2, '*', '5 * 2', 10)
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                prob, ans = fun_operator(num1, num2, operator)
                self.assertEqual(prob, expected_problem)
                self.assertEqual(ans, expected_answer)
            
if __name__ == "__main__":
    unittest.main()
