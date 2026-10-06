from rest_framework import serializers
from .models import Order, OrderItem
from shop.models import ShopItem

class OrderItemSerializer(serializers.ModelSerializer):
    # Pull in the artwork name directly for easy reading when viewing order payloads
    shop_item_title = serializers.CharField(source='shop_item.title', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'shop_item', 'shop_item_title', 'format_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    # This enables handling multiple line items inside a single order payload
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id', 'customer_name', 'customer_email', 'customer_phone',
            'address', 'city', 'state', 'zip_code', 'country', 'delivery_notes',
            'total_ghc', 'total_usd', 'payment_method', 'payment_reference',
            'payment_status', 'order_status', 'items', 'created_at'
        ]

    def create(self, validated_data):
        # Extract the nested order line items away from the core customer info
        items_data = validated_data.pop('items')
        
        # Save the master Order record first
        order = Order.objects.create(**validated_data)
        
        # Loop through and create each individual item tied back to this master order
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order