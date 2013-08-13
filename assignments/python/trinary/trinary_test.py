from trinary import Trinary
import unittest

class TrinaryTest(unittest.TestCase):
    def test_trinary_1_is_decimal_1(self):
        self.assertEqual(1, int(Trinary("1")))

    def test_trinary_2_is_decimal_2(self):
        self.assertEqual(2, int(Trinary("2")))

    def test_trinary_10_is_decimal_3(self):
        self.assertEqual(3, int(Trinary("10")))

    def test_trinary_11_is_decimal_4(self):
        self.assertEqual(4, int(Trinary("11")))

    def test_trinary_100_is_decimal_9(self):
        self.assertEqual(9, int(Trinary("100")))

    def test_trinary_112_is_decimal_14(self):
        self.assertEqual(14, int(Trinary("112")))

    def test_trinary_222_is_26(self):
        self.assertEqual(26, int(Trinary("222")))

    def test_trinary_1122000120_is_32091(self):
        self.assertEqual(32091, int(Trinary("1122000120")))

    def test_invalid_trinary_is_decimal_0(self):
        self.assertEqual(0, int(Trinary("carrot")))

if __name__ == '__main__':
    unittest.main()
