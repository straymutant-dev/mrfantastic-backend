from rest_framework import serializers
from .models import ShopItem, ItemFormat, Category

class CategorySerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='get_code_display', read_only=True)

    class Meta:
        model = Category
        fields = ['code', 'display_name']

class ItemFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFormat
        fields = ['id', 'name', 'price']

class ShopItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    formats = ItemFormatSerializer(many=True, read_only=True)

    class Meta:
        model = ShopItem
        fields = [
            'id', 'title', 'description', 'image', 
            'categories', 'base_price', 'is_available', 
            'formats', 'created_at'
        ]