from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class CumulativeSumsTestCase(BaseTestCaseMixin, TestCase):

    def _get_test(self):
        return sp80022suite.cumulative_sums

    def test_nist_description(self):

        self.assertAlmostEqual(
            0.4116588,
            sp80022suite.cumulative_sums(self.str_to_bytes("1011010111"))
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.114866,
            sp80022suite.cumulative_sums(self.EXAMPLE_EPSILON)
        )
