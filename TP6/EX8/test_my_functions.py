import unittest
from my_functions import safe_division, convert_to_int, read_file, set_age, NegativeAgeError

class TestExceptions(unittest.TestCase):

    def test_safe_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)

    def test_convert_to_int_invalid(self):
        with self.assertRaises(ValueError):
            convert_to_int("abc")

    def test_set_age_negative(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-1)

if __name__ == '__main__':
    unittest.main()
