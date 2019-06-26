import random
from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class RandomExcursionsTestCase(BaseTestCaseMixin, TestCase):

    def _get_test(self):
        return sp80022suite.random_excursions

    def test_constant(self):
        with self.assertRaises(ValueError):
            sp80022suite.random_excursions(bytes([0] * self.SEQUENCE_LENGTH))

    def test_nist_description(self):
        with self.assertRaises(ValueError):
            sp80022suite.random_excursions(self.str_to_bytes("1011010111"))

    def test_random(self):
        with self.assertRaises(ValueError):
            random.seed(0)
            sequence = bytes([random.choice((0, 1)) for _ in range(self.SEQUENCE_LENGTH)])
            sp80022suite.random_excursions(sequence)

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.007779,
            sp80022suite.random_excursions(self.str_to_bytes(self.e_binary_digits(1e6)))
        )
