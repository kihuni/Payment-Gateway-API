from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class PaymentTests(APITestCase):
    def test_create_payment(self):
        url = reverse('initiate-payment')
        data = {
            "customer_name": "Jane Doe",
            "customer_email": "jane@example.com",
            "amount": 25.00
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_payment_status_not_found(self):
        url = reverse('payment-status', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

