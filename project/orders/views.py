# views.py
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .send_sms import send_sms_notification

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # After the order has been created, send sms
        name = instance.user.username
        phone = ["+254110456655"]
        message = f"Order with code {instance.code} was placed successfully by {name}"
        send_sms_notification(message, phone)