import unittest

def add_integer(a, b):
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b

class TestAddIntegerFunction(unittest.TestCase):

    def test_adding_tuple(self):
        with self.assertRaises(TypeError, msg="a must be an integer"):
            add_integer((1, 1))

    def test_adding_number_and_list(self):
        with self.assertRaises(TypeError, msg="b must be an integer"):
            add_integer(123, [])

    def test_passing_string(self):
        with self.assertRaises(TypeError, msg="a must be an integer"):
            add_integer("Hello")

    def test_adding_two_float_numbers(self):
        result = add_integer(2.9, 2.9)
        self.assertEqual(result, 4)

    def test_subtracting_98_and_1(self):
        result = add_integer(-1)
        self.assertEqual(result, 97)

    def test_overflow_case_1(self):
        with self.assertRaises(OverflowError, msg="cannot convert float infinity to integer"):
            add_integer(float('inf'), 0)

    def test_overflow_case_2(self):
        with self.assertRaises(OverflowError, msg="cannot convert float infinity to integer"):
            add_integer(float('inf'), float('-inf'))

    def test_nan_case(self):
        with self.assertRaises(ValueError, msg="cannot convert float NaN to integer"):
            add_integer(0, float('nan'))

if __name__ == '__main__':
    unittest.main()
