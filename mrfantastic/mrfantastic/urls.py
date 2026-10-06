from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from shop.views import ShopItemPublicViewSet, AdminShopItemViewSet
from portfolio.views import PortfolioItemPublicViewSet, AdminPortfolioItemViewSet
from orders.views import OrderCreatePublicView, OrderVerifyPaymentView, AdminOrderViewSet
from admin_dashboard.views import DashboardStatsView

# Initialize DRF's automatic routing for viewsets
router = DefaultRouter()
router.register(r'shop/items', ShopItemPublicViewSet, basename='public-shop')
router.register(r'portfolio/items', PortfolioItemPublicViewSet, basename='public-portfolio')

# Protected admin routes for managing shop, portfolio, and orders
router.register(r'admin/shop/items', AdminShopItemViewSet, basename='admin-shop')
router.register(r'admin/portfolio/items', AdminPortfolioItemViewSet, basename='admin-portfolio')
router.register(r'admin/orders', AdminOrderViewSet, basename='admin-orders')

# 🚀 Global configuration hooks mapping all branding layouts to the custom profile
admin.site.site_url = 'http://localhost:3000'
admin.site.site_header = "M.F. ADMINISTRATION"
admin.site.site_title = "M.F. Administration Control Room"
admin.site.index_title = "Control Room Workspace"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Order workflow urls
    path('api/orders/create/', OrderCreatePublicView.as_view(), name='public-order-create'),
    path('api/orders/verify-payment/', OrderVerifyPaymentView.as_view(), name='public-verify-payment'),
    
    # Dashboard metrics endpoint
    path('api/admin/dashboard-stats/', DashboardStatsView.as_view(), name='admin-stats'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)