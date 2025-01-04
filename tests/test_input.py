import unittest
from unittest.mock import patch
from inp_kwargs import input_int

class TestInputInt(unittest.TestCase):

    def test_invalid_integer_input(self):
        with patch('builtins.input', side_effect=['abc', '50']):
            with patch('builtins.print') as mock_print:
                result = input_int("Enter a number: ", type_error_message="Invalid input!")
                mock_print.assert_called_with("Invalid input!")
                self.assertEqual(result, 50)

    def test_below_min_value(self):
        with patch('builtins.input', side_effect=['0', '50']):
            result = input_int("Enter a number: ", min_value=1, min_value_error_message="Too low!")
            self.assertEqual(result, 50)

    def test_above_max_value(self):
        with patch('builtins.input', side_effect=['150', '50']):
            result = input_int("Enter a number: ", max_value=100, max_value_error_message="Too high!")
            self.assertEqual(result, 50)

    def test_not_in_range(self):
        with patch('builtins.input', side_effect=['5', '15']):
            result = input_int("Enter a number: ", range=range(10, 20), range_error_message="Not in range!")
            self.assertEqual(result, 15)

    def test_not_in_allowed_values(self):
        with patch('builtins.input', side_effect=['3', '5']):
            result = input_int("Enter a number: ", allowed_values=[1, 2, 5], allowed_error_message="Not allowed!")
            self.assertEqual(result, 5)

    def test_not_even(self):
        with patch('builtins.input', side_effect=['3', '4']):
            result = input_int("Enter a number: ", even=True, even_error_message="Not even!")
            self.assertEqual(result, 4)

    def test_not_odd(self):
        with patch('builtins.input', side_effect=['4', '3']):
            result = input_int("Enter a number: ", odd=True, odd_error_message="Not odd!")
            self.assertEqual(result, 3)

    def test_not_multiple_of(self):
        with patch('builtins.input', side_effect=['7', '6']):
            result = input_int("Enter a number: ", multiple_of=3, multiple_error_message="Not a multiple!")
            self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()