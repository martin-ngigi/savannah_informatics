# serializers.py
from rest_framework import serializers
from .models import Order
from items.serializers import ItemSerializer
from profile_account.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    # items = ItemSerializer(read_only=True, many=True)
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        if self.context['request'].method == 'GET':
            # Serialize 'items' and 'user' only for GET requests
            representation = super().to_representation(instance)
            representation['items'] = ItemSerializer(instance.items.all(), many=True).data
            representation['user'] = UserSerializer(instance.user).data
            return representation
        else:
            # Exclude 'items' and 'user' for other HTTP methods (POST, PUT)
            return super().to_representation(instance)