import unittest
from app import create_app


class HomeBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('test')
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_valid_input(self):
        house_value = 200000
        down_payment = 100000
        interest = 4
        periodic = 30

        response = self.client.post('/', data=dict(house_value=house_value, down_payment=down_payment, interest=interest, periodic=periodic))
        self.assertEqual(200, response.status_code)

    def test_invalid_input(self):
        down_payment = 'aaa'
        total_payment = 200000
        interest = -1

        response = self.client.post('/', data=dict(down_payment=down_payment, total_payment=total_payment, interest=interest))
        self.assertEqual(400, response.status_code)
