import random
from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class BlockFrequencyTestCase(BaseTestCaseMixin, TestCase):

    DEFAULT_ARGS = [10]

    def _get_test(self):
        return sp80022suite.block_frequency

    def test_0011(self):
        sequence = b"\x00\x00\x01\x01" * self.SEQUENCE_LENGTH
        self.assertPass(sp80022suite.block_frequency(1, sequence))
        self.assertFail(sp80022suite.block_frequency(2, sequence))
        self.assertPass(sp80022suite.block_frequency(4, sequence))

    def test_000111(self):
        sequence = b"\x00\x00\x00\x01\x01\x01" * self.SEQUENCE_LENGTH
        self.assertFail(sp80022suite.block_frequency(3, sequence))

    def test_constant(self):
        for val in [b"\x00", b"\x01"]:
            for block_length in [2, 8, 16]:
                sequence = val * self.SEQUENCE_LENGTH
                self.assertAlmostEqual(
                    sp80022suite.block_frequency(block_length, sequence),
                    0.0,
                    places=10
                )

    def test_nist_description(self):
        self.assertAlmostEqual(
            0.801252,
            sp80022suite.block_frequency(3, self.str_to_bytes("0110011010"))
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.706438,
            sp80022suite.block_frequency(10, self.EXAMPLE_EPSILON)
        )
