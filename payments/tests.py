# payments/tests.py

from django.test import TestCase
from .models import Payment

class PaymentModelTest(TestCase):
    def test_create_payment(self):
        payment = Payment.objects.create(
            customer_name="Test User",
            customer_email="test@example.com",
            amount=10.00,
            paypal_payment_id="PAY-ID",
            status="created"
        )
        self.assertEqual(payment.customer_name, "Test User")
