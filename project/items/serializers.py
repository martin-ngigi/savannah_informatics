from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ['id', 'name', 'description', 'price']
        fields = '__all__'

