# payments/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
import paypalrestsdk

class PaymentCreateView(APIView):
    def post(self, request):
        data = request.data
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": { "payment_method": "paypal" },
            "redirect_urls": {
                "return_url": "http://localhost:8000/payment/execute",
                "cancel_url": "http://localhost:8000/payment/cancel"
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Business Payment",
                        "sku": "001",
                        "price": str(data['amount']),
                        "currency": "USD",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": str(data['amount']),
                    "currency": "USD"
                },
                "description": f"Payment by {data['customer_name']}"
            }]
        })

        if payment.create():
            new_payment = Payment.objects.create(
                customer_name=data['customer_name'],
                customer_email=data['customer_email'],
                amount=data['amount'],
                paypal_payment_id=payment.id,
                status='created'
            )
            return Response({
                "status": "success",
                "payment_id": new_payment.id,
                "paypal_payment_id": payment.id,
                "approval_url": next(link.href for link in payment.links if link.rel == "approval_url")
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "message": payment.error}, status=400)

class PaymentStatusView(APIView):
    def get(self, request, pk):
        try:
            payment = Payment.objects.get(id=pk)
            serializer = PaymentSerializer(payment)
            return Response({
                "payment": serializer.data,
                "status": "success",
                "message": "Payment details retrieved successfully."
            }, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Payment not found."
            }, status=status.HTTP_404_NOT_FOUND)
