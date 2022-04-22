import unittest
from tasks.factorial import calculate_factorial


class TestFactorialCalculation(unittest.TestCase):
    def test_calculate_factorial_should_raise_value_error_when_input_number_is_negative(self):
        number_negative = -5
        with self.assertRaises(ValueError):
            calculate_factorial(number_negative)

    def test_calculate_factorial_should_return_one_when_input_number_is_zero(self):
        number = 0
        expected_result = 1
        actual_result = calculate_factorial(number)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_factorial_should_return_two_when_input_number_is_two(self):
        number = 2
        expected_result = 2
        actual_result = calculate_factorial(number)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_factorial_should_return_correct_factorial_when_input_number_is_non_negative_integer(self):
        number = 5
        expected_result = 120
        actual_result = calculate_factorial(number)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
