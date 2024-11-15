import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if the random number generated by function_A is within the specified range
        min_val = 1
        max_val = 10
        rand_num = function_A(min_val, max_val)
        self.assertGreaterEqual(rand_num, min_val)  # Check if it's greater than or equal to min
        self.assertLessEqual(rand_num, max_val)  # Check if it's less than or equal to max

    def test_function_B(self):
        # Test if function_B correctly formats a simple addition problem
        num1 = 5
        num2 = 3
        result = function_B(num1, num2, '+')
        self.assertEqual(result, '5 + 3 = 8')

    def test_function_C(self):
        # Test if function_C returns the correct problem and answer for a simple subtraction problem
        num1 = 9
        num2 = 4
        problem, answer = function_C(num1, num2, '-')
        self.assertEqual(problem, '9 - 4')
        self.assertEqual(answer, 5)


if __name__ == "__main__":
    unittest.main()

