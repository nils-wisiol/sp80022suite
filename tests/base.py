import math
import random
from decimal import Decimal, getcontext

from tests.e_high_precision import E_STRING


class BaseTestCaseMixin:

    EXAMPLE_EPSILON = "11001001000011111101101010100010001000010110100011" \
                      "00001000110100110001001100011001100010100010111000"
    ALPHA = 0.1
    SEQUENCE_LENGTH = 10000
    DEFAULT_ARGS = []

    E_BINARY_DIGITS = ""
    RANDOM_01_BYTES = bytes()

    # noinspection PyPep8Naming
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.EXAMPLE_EPSILON = bytes([1 if c == "1" else 0 for c in self.EXAMPLE_EPSILON])

    # noinspection PyPep8Naming
    def assertAlmostEqual(self, first: float, second: float, places: int = 6, **kwargs) -> None:
        super().assertAlmostEqual(first, second, places, **kwargs)

    # noinspection PyPep8Naming
    def assertPass(self, result):
        return self.assertGreater(result, self.ALPHA, "Expected the test to pass, but got p-value of %f <= %f." %
                                  (result, self.ALPHA))

    # noinspection PyPep8Naming
    def assertFail(self, result):
        return self.assertLess(result, self.ALPHA, "Expected the test to fail, but got p-value of %f >= %f." %
                               (result, self.ALPHA))

    @classmethod
    def e_binary_digits(cls, digits2):
        digits2 = int(digits2)
        if len(cls.E_BINARY_DIGITS) < digits2:
            digits10 = int(math.ceil(digits2 / math.log(10, 2))) + 1
            getcontext().prec = digits10
            precision = Decimal(2) ** Decimal(digits2)
            result = bin(int(Decimal(E_STRING[:digits10+1]) * precision))[2:][:digits2]
            cls.E_BINARY_DIGITS = result
        return cls.E_BINARY_DIGITS[:digits2]

    @staticmethod
    def str_to_bytes(string):
        return bytes([1 if c == "1" else 0 for c in string])

    @classmethod
    def random_01_bytes(cls, length):
        if len(cls.RANDOM_01_BYTES) < length:
            random.seed(0)
            cls.RANDOM_01_BYTES = bytes([random.choice((0,1)) for _ in range(length)])
        return cls.RANDOM_01_BYTES[:length]

    @classmethod
    def random_01_bytes_g_sha_1_fips_186_2(cls, length):
        # TODO how to generate bits using G-SHA-1 (FIPS 186-2)?
        raise NotImplementedError

    def _get_test(self):
        raise NotImplementedError

    def test_random(self):
        random.seed(0)
        sequence = bytes([random.choice((0, 1)) for _ in range(self.SEQUENCE_LENGTH)])
        self.assertPass(self._get_test()(*self.DEFAULT_ARGS, sequence))

    def test_constant(self):
        self.assertFail(self._get_test()(*self.DEFAULT_ARGS, bytes([0] * self.SEQUENCE_LENGTH)))
        self.assertFail(self._get_test()(*self.DEFAULT_ARGS, bytes([1] * self.SEQUENCE_LENGTH)))

    def test_nist_description(self):
        raise NotImplementedError

    def test_nist_example(self):
        raise NotImplementedError
