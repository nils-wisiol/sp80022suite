import random
from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class FrequencyTestCase(BaseTestCaseMixin, TestCase):

    def _get_test(self):
        return sp80022suite.frequency

    def test_01(self):
        sequence = b"\x00\x01" * self.SEQUENCE_LENGTH
        self.assertEqual(
            sp80022suite.frequency(sequence),
            1.0
        )

    def test_nist_description(self):
        self.assertAlmostEqual(
            0.527089,
            sp80022suite.frequency(self.str_to_bytes("1011010101")),
            places=6
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.109599,
            sp80022suite.frequency(self.EXAMPLE_EPSILON),
            places=6
        )
