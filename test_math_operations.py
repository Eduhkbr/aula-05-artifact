import unittest
from math_operations import is_prime


class TestMathOperations(unittest.TestCase):

    def test_is_prime_positive(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))


if __name__ == '__main__':
    unittest.main()
