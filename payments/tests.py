# payments/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
import paypalrestsdk

class PaymentTests(APITestCase):
    def setUp(self):
        # Mock PayPal payment
        self.mock_payment = paypalrestsdk.Payment({
            "id": "PAY-123456",
            "links": [{"rel": "approval_url", "href": "https://paypal.com/approve"}]
        })
        self.mock_payment.create = lambda: True

    @patch('paypalrestsdk.Payment')
    def test_get_payment_status_success(self, MockPayment):
        MockPayment.return_value = self.mock_payment
        create_url = reverse('initiate-payment')
        data = {
            "customer_name": "John Smith",
            "customer_email": "john@example.com",
            "amount": 30.00
        }
        create_response = self.client.post(create_url, data, format='json')
        payment_id = create_response.data.get("payment_id")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        status_url = reverse('payment-status', args=[payment_id])
        response = self.client.get(status_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payment"]["customer_name"], "John Smith")

    def test_create_payment_missing_fields(self):
        url = reverse('initiate-payment')
        data = {
            "customer_email": "incomplete@example.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_payment_invalid_amount(self):
        url = reverse('initiate-payment')
        data = {
            "customer_name": "Test User",
            "customer_email": "test@example.com",
            "amount": "invalid"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)