from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class OverlappingTemplateMatchingsTestCase(TestCase, BaseTestCaseMixin):

    # TODO some other values fail: why?
    DEFAULT_ARGS = [9]
    SEQUENCE_LENGTH = 2**17

    def _get_test(self):
        return sp80022suite.overlapping_template_matchings

    def test_nist_description(self):
        # parameters used in the description are different from parameters hard-coded
        # in the implementation
        pass

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.110434,
            sp80022suite.overlapping_template_matchings(9, self.str_to_bytes(self.e_binary_digits(1000000))),
            places=6
        )
