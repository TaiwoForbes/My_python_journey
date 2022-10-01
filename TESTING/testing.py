from myFunction import multiply
import unittest


class TestMultiply(unittest.TestCase):

    def test_with_two_postive(self):
        self.assertEqual(multiply(17,19), 17 * 19)

    def test_with_two_zero(self):
        self.assertEqual(multiply(0,0), 0 * 0)
    def test_with_two_negative_values(self):
        self.assertEqual(multiply(-19,-17), -17 * -19)
    