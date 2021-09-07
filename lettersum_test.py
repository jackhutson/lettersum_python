from lettersum import letter_sum
import unittest
from lettersum import letter_sum

class LetterSumTests(unittest.TestCase):

    def test_if_a_returns_1(self):
        self.assertEqual(letter_sum("a"), 1)

    def test_if_empty_string_returns_0(self):
        self.assertEqual(letter_sum(""), 0)

    def test_if_z_returns_26(self):
        self.assertEqual(letter_sum("z"), 26)

    def test_if_uppercase_a_returns_1(self):
        self.assertEqual(letter_sum("A"), 1)

    def test_cab_returns_6(self):
        self.assertEqual(letter_sum("cab"), 6)

    def test_excellent_returns_100(self):
        self.assertEqual(letter_sum("excellent"), 100)

    def test_microspectrophotometries_317(self):
        self.assertEqual(letter_sum("microspectrophotometries"), 317)