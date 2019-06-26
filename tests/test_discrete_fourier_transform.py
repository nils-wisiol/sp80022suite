from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class DiscreteFourierTransformTestCase(BaseTestCaseMixin, TestCase):

    def _get_test(self):
        return sp80022suite.discrete_fourier_transform

    def test_nist_description(self):
        self.assertAlmostEqual(
            0.468160,  # NIST documented 0.029523, but seems false
            sp80022suite.discrete_fourier_transform(self.str_to_bytes("1001010011"))
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.646355,  # NIST documented 0.168669, but seems false
            sp80022suite.discrete_fourier_transform(self.EXAMPLE_EPSILON)
        )
