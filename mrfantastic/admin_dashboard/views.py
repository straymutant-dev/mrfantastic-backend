from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Sum
from shop.models import ShopItem
from portfolio.models import PortfolioItem
from orders.models import Order

class DashboardStatsView(APIView):
    """
    Protected Admin endpoint returning analytical data for dashboard counter widgets.
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        # Calculate Total revenue gathered across completed orders
        total_revenue = Order.objects.filter(payment_status='completed').aggregate(Sum('total_ghc'))['total_ghc__sum'] or 0.00
        
        # Gather aggregate item parameters
        total_shop_items = ShopItem.objects.count()
        total_portfolio_items = PortfolioItem.objects.count()
        total_orders_count = Order.objects.count()

        # Breakdown states matching your UI tracking fields
        orders_by_status = {
            "received": Order.objects.filter(order_status='received').count(),
            "processing": Order.objects.filter(order_status='processing').count(),
            "shipped": Order.objects.filter(order_status='shipped').count(),
            "delivered": Order.objects.filter(order_status='delivered').count(),
        }

        return Response({
            "total_revenue_ghc": total_revenue,
            "total_orders": total_orders_count,
            "total_shop_artworks": total_shop_items,
            "total_portfolio_artworks": total_portfolio_items,
            "status_metrics": orders_by_status
        })