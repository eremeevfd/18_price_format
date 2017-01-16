import unittest
from format_price import format_price


class TestFormatPriceMethod(unittest.TestCase):
    def test_format_price_without_fraction(self):
        self.assertEqual(format_price('3245.0000000'), '3 245')

    def test_format_price_with_fraction(self):
        self.assertEqual(format_price('3245.12123123123'), '3 245.12')

    def test_format_price_returns_None(self):
        self.assertIsNone(format_price('asdf'))
        self.assertIsNone(format_price('3456.775667.65'))
        self.assertIsNone(format_price('-3'))
        self.assertIsNone(format_price('0'))


if __name__ == '__main__':
    unittest.main()
