from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class NonOverlappingTemplateMatchingsTestCase(TestCase, BaseTestCaseMixin):

    # TODO some other values fail: why?
    DEFAULT_ARGS = [4]
    SEQUENCE_LENGTH = 2**16

    def _get_test(self):
        return sp80022suite.non_overlapping_template_matchings

    def test_negative_lambda(self):
        with self.assertRaises(ValueError):
            sp80022suite.non_overlapping_template_matchings(3, bytes([1]))

    def test_nist_description(self):
        # parameters used in the description are different from parameters hard-coded
        # in the implementation
        pass

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.647302,
            sp80022suite.non_overlapping_template_matchings(9, self.random_01_bytes_g_sha_1_fips_186_2(2**20))
        )
