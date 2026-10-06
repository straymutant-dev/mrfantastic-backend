from rest_framework import serializers
from .models import PortfolioItem
from shop.serializers import CategorySerializer

class PortfolioItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioItem
        fields = ['id', 'title', 'image', 'categories', 'created_at']