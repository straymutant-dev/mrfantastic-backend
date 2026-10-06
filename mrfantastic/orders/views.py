from rest_framework import generics, viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderCreatePublicView(generics.CreateAPIView):
    """
    Public API endpoint for processing checkout data and saving incoming orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderVerifyPaymentView(APIView):
    """
    Public endpoint hit by the frontend after a Paystack payment completes
    to securely mark the order as paid in the database.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        reference = request.data.get('payment_reference')
        if not reference:
            return Response({"error": "Payment reference is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            order = Order.objects.get(payment_reference=reference)
            
            # NOTE: In Phase 4, we will add the live Paystack server-to-server request here.
            # For Phase 1 validation, we simulate a successful transaction verification.
            order.payment_status = 'completed'
            order.order_status = 'processing'
            order.save()
            
            return Response({
                "message": "Payment verified successfully.", 
                "payment_status": order.payment_status,
                "order_status": order.order_status
            }, status=status.HTTP_200_OK)
            
        except Order.DoesNotExist:
            return Response({
                "error": "Order not found with that payment reference."
            }, status=status.HTTP_404_NOT_FOUND)

class AdminOrderViewSet(viewsets.ModelViewSet):
    """
    Protected Admin endpoint to view, inspect, and update customer order fulfillment statuses.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser] # Restricts access to you and the artist only