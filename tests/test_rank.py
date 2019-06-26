import math
from decimal import Decimal
from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin
from tests.e_high_precision import E_STRING


class RankTestCase(BaseTestCaseMixin, TestCase):

    def _get_test(self):
        return sp80022suite.rank

    def test_e(self):
        self.assertEqual(
            math.e,
            float(Decimal(E_STRING[:20]))
        )

    def test_e_binary_digits(self):
        expected = "10101101111110000101010001011000101000101011101101001010" \
                   "10011010101011111101110001010110001000000010011100111101"
        digits2 = len(expected)
        self.assertEqual(
            expected,
            self.e_binary_digits(digits2)
        )

    def test_nist_description(self):
        # parameters used in the description are different from parameters hard-coded
        # in the implementation
        pass

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.532069,
            sp80022suite.rank(self.str_to_bytes(self.e_binary_digits(100000))),
            places=6
        )
