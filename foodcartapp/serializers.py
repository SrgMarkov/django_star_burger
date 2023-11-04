from rest_framework.serializers import ModelSerializer

from .models import Order, OrderList


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['product', 'quantity']


class OrderSerializer(ModelSerializer):
    products = OrderListSerializer(many=True, allow_empty=False, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'firstname', 'lastname', 'phonenumber', 'address',
                  'products']
