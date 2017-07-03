import unittest

from app.services.payment_services import calculate_monthly_payment


class PaymentServicesTestCase(unittest.TestCase):

    def test_calculate_monthly_payment(self):
        expected_monthly_payment_1 = 1194
        actual_monthly_payment_1 = calculate_monthly_payment(
                house_value=300000,
                down_payment=50000,
                interest_in_percents=4,
                periodic_in_years=30)
        self.assertEqual(expected_monthly_payment_1, actual_monthly_payment_1)

        expected_monthly_payment_2 = 4756
        actual_monthly_payment_2 = calculate_monthly_payment(
                house_value=300000,
                down_payment=30000,
                interest_in_percents=2.2,
                periodic_in_years=5)
        self.assertEqual(expected_monthly_payment_2, actual_monthly_payment_2)
