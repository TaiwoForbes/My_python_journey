from myFunction import multiply_better
import unittest


class TestMultiply(unittest.TestCase):

    def test_with_two_postive(self):
        self.assertEqual(multiply_better(17,19), 17 * 19)

    def test_with_two_zero(self):
        self.assertEqual(multiply_better(0,0), 0 * 0)
    def test_with_two_negative_values(self):
        self.assertEqual(multiply_better(-19,-17), -17 * -19)
    def test_with_one_positive(self):
        self.assertEqual(multiply_better(19,-17), 19 * -17)
        self.assertEqual(multiply_better(-17,19), -17 * 19)