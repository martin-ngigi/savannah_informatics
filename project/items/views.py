from django.shortcuts import render

# Create your views here.

from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer