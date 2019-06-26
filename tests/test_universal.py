from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class UniversalTestCase(BaseTestCaseMixin, TestCase):

    SEQUENCE_LENGTH = 388840

    def _get_test(self):
        return sp80022suite.universal

    def test_nist_description(self):
        # parameters used in the description are different from parameters hard-coded
        # in the implementation
        pass

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.427733,
            sp80022suite.universal(self.random_01_bytes_g_sha_1_fips_186_2(1048576))
        )
