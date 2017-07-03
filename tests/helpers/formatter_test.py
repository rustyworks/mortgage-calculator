import unittest
from app.helpers.formatter import separate_number


class FormatterTestCase(unittest.TestCase):

    def test_separate_number(self):
        expected_currency_1 = '10,000'
        actual_currency_1 = separate_number(10000)
        self.assertEqual(expected_currency_1, actual_currency_1)

        expected_currency_2 = '10.000'
        actual_currency_2 = separate_number(10000, '.')
        self.assertEqual(expected_currency_2, actual_currency_2)
