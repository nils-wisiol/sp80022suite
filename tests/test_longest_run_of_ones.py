import random
from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class LongestRunOfOnesTestCase(BaseTestCaseMixin, TestCase):

    EXAMPLE_EPSILON = "11001100000101010110110001001100111000000000001001" \
                      "00110101010001000100111101011010000000110101111100" \
                      "1100111001101101100010110010"

    def _get_test(self):
        return sp80022suite.longest_run_of_ones

    def test_long_zero(self):
        random_head = [random.choice((0, 1)) for _ in range(self.SEQUENCE_LENGTH)]
        ones = [1] * self.SEQUENCE_LENGTH
        zeros = [0] * self.SEQUENCE_LENGTH
        random_tail = [random.choice((0, 1)) for _ in range(self.SEQUENCE_LENGTH)]
        self.assertFail(sp80022suite.longest_run_of_ones(bytes(random_head + ones + zeros + random_tail)))
        self.assertFail(sp80022suite.longest_run_of_ones(bytes(random_head + zeros + ones + random_tail)))

    def test_nist_description(self):
        # same as the NIST example
        pass

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.180609,
            sp80022suite.longest_run_of_ones(self.EXAMPLE_EPSILON),
            places=6
        )
