from rest_framework import viewsets, permissions
from .models import PortfolioItem
from .serializers import PortfolioItemSerializer

class PortfolioItemPublicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public API endpoint to fetch the complete portfolio image grid.
    """
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer
    permission_classes = [permissions.AllowAny]

class AdminPortfolioItemViewSet(viewsets.ModelViewSet):
    """
    Protected Admin endpoint allowing full creation, editing, and deletion of portfolio showcase galleries.
    """
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer
    permission_classes = [permissions.IsAdminUser]