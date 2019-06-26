from unittest import TestCase

import sp80022suite

from tests.base import BaseTestCaseMixin


class SerialTestCase(BaseTestCaseMixin, TestCase):

    DEFAULT_ARGS = [6]

    def _get_test(self):
        return sp80022suite.serial

    def test_nist_description(self):
        # in serial.c:23, input to cephes_igamc is as documented, i.e.:
        #   pow(2, m-1)/2 --> 2.0
        #   del1/2.0      --> 0.8
        # However, cephes_igamc(...) is then evaluated to 0.808792, different from the
        # documented value of 0.8805.
        #
        # This documented result of the complementary incomplete gamma function on input
        # 2.0, 0.8 seems to be false: the scipy implementation agrees with the cephes
        # implementation, the result should therefore actually be:
        #   p_value1      --> 0.8087921354109986
        self.assertAlmostEqual(
            0.670320,  # TODO NIST documented 0.8805, but I suspect a mistake, see comment above
            sp80022suite.serial(3, self.str_to_bytes("0011011101"))
        )

    def test_nist_example(self):
        self.assertAlmostEqual(
            0.561915,
            sp80022suite.serial(2, self.str_to_bytes(self.e_binary_digits(1e6)))
        )
