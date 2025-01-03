import unittest
from unittest.mock import patch
from inp_kwargs import input_int

class TestInputInt(unittest.TestCase):

    def test_invalid_integer_input(self):
        with patch('builtins.input', side_effect=['abc', '50']):
            result = input_int("Enter a number: ", error_txt="Invalid input!")
            self.assertEqual(result, 50)

    def test_below_min_value(self):
        with patch('builtins.input', side_effect=['0', '50']):
            result = input_int("Enter a number: ", min_value=1, error_min="Too low!")
            self.assertEqual(result, 50)

    def test_above_max_value(self):
        with patch('builtins.input', side_effect=['150', '50']):
            result = input_int("Enter a number: ", max_value=100, error_max="Too high!")
            self.assertEqual(result, 50)

if __name__ == "__main__":
    unittest.main()