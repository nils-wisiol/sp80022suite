import random
from typing import Any
from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class RunsTestCase(BaseTestCaseMixin, TestCase):

    def _get_test(self):
        return sp80022suite.runs

    def test_fails_if_not_applicable(self):
        sequence = bytes([0, 0]) * self.SEQUENCE_LENGTH
        self.assertFail(sp80022suite.runs(sequence))
        self.assertEqual(
            sp80022suite.runs(sequence),
            0.0
        )

    def test_oscillation_too_fast(self):
        self.assertFail(sp80022suite.runs(bytes([0, 1, 0, 1, 0, 1]) * self.SEQUENCE_LENGTH))
        self.assertFail(sp80022suite.runs(bytes([0, 1, 0, 1, 1, 0]) * self.SEQUENCE_LENGTH))
        self.assertFail(sp80022suite.runs(bytes([0, 1, 0, 1, 0, 0]) * self.SEQUENCE_LENGTH))

    def test_oscillation_too_slow(self):
        self.assertFail(sp80022suite.runs(bytes([0, 0, 0, 0, 0, 1]) * self.SEQUENCE_LENGTH))
        self.assertFail(sp80022suite.runs(bytes([1, 1, 1, 1, 1, 0]) * self.SEQUENCE_LENGTH))
        self.assertFail(sp80022suite.runs(bytes([1, 1, 1, 0, 1, 1]) * self.SEQUENCE_LENGTH))

    def test_long_zero(self):
        random_head = [random.choice((0, 1)) for _ in range(self.SEQUENCE_LENGTH)]
        ones = [1] * self.SEQUENCE_LENGTH
        zeros = [0] * self.SEQUENCE_LENGTH
        random_tail = [random.choice((0, 1)) for _ in range(self.SEQUENCE_LENGTH)]
        self.assertFail(sp80022suite.runs(bytes(random_head + ones + zeros + random_tail)))
        self.assertFail(sp80022suite.runs(bytes(random_head + zeros + ones + random_tail)))

    def test_nist_description(self):
        self.assertAlmostEqual(
            0.147232,
            sp80022suite.runs(self.str_to_bytes("1001101011"))
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.500798,
            sp80022suite.runs(self.EXAMPLE_EPSILON),
            places=6
        )
