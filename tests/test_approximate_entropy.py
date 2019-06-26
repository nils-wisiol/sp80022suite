from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class ApproximateEntropyTestCase(BaseTestCaseMixin, TestCase):

    DEFAULT_ARGS = [6]

    def _get_test(self):
        return sp80022suite.approximate_entropy

    def test_nist_description(self):

        self.assertAlmostEqual(
            0.261961,
            sp80022suite.approximate_entropy(3, self.str_to_bytes("0100110101"))
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.235301,
            sp80022suite.approximate_entropy(2, self.EXAMPLE_EPSILON)
        )
