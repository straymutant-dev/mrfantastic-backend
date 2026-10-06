from rest_framework import viewsets, permissions
from .models import ShopItem
from .serializers import ShopItemSerializer

class ShopItemPublicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public API endpoint to view active shop items and their format options.
    """
    queryset = ShopItem.objects.filter(is_available=True)
    serializer_class = ShopItemSerializer
    permission_classes = [permissions.AllowAny]

class AdminShopItemViewSet(viewsets.ModelViewSet):
    """
    Protected Admin endpoint allowing full creation, editing, and deletion of shop inventory items.
    """
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    permission_classes = [permissions.IsAdminUser]