from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class RankTestCase(BaseTestCaseMixin, TestCase):

    DEFAULT_ARGS = [1000]

    def _get_test(self):
        return sp80022suite.linear_complexity

    def test_nist_description(self):
        # result not specified by SP-800-22 Rev 1a
        pass

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.845406,
            sp80022suite.linear_complexity(1000, self.str_to_bytes(self.e_binary_digits(1e6))),
            places=6
        )
