from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    # Make line-item pricing details read-only to lock down transaction records
    readonly_fields = ('shop_item', 'format_name', 'quantity', 'price')
    can_delete = False  # Prevents accidental deletion of purchased products from an order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # ── 1. DASHBOARD OVERVIEW LIST CONFIGURATION ───────────────────────────
    list_display = ('id', 'customer_name', 'total_ghc', 'payment_status', 'order_status', 'created_at')
    list_filter = ('payment_status', 'order_status', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'payment_reference')
    
    # Fast Tracking: Toggle order status workflows directly from the main list view
    list_editable = ('payment_status', 'order_status')
    
    # ── 2. IMMUTABLE TRANSACTION SECURITY DETECTOR ─────────────────────────
    # Protects customer details and checkout balances from manual modification
    readonly_fields = (
        'payment_reference', 'payment_method', 'total_ghc', 'total_usd', 
        'customer_name', 'customer_email', 'customer_phone',
        'address', 'city', 'state', 'zip_code', 'country', 'delivery_notes',
        'created_at', 'updated_at'
    )
    
    # ── 3. PREMIUM COMPONENT LAYOUT FIELDSETS ──────────────────────────────
    # Groups data fields into clean, scannable structural blocks
    fieldsets = (
        ('Fulfillment & Gateway Status', {
            'fields': ('order_status', 'payment_status', 'payment_method', 'payment_reference'),
            'description': 'Manage order delivery stages and inspect payment tracking keys.'
        }),
        ('Customer Account Details', {
            'fields': ('customer_name', 'customer_email', 'customer_phone')
        }),
        ('Shipping Destination Matrix', {
            'fields': ('address', 'city', 'state', 'zip_code', 'country', 'delivery_notes'),
            'classes': ('collapse',),  # Keeps layout clean by making shipping data collapsible
        }),
        ('Financial Ledger Summary', {
            'fields': ('total_ghc', 'total_usd')
        }),
        ('System Log Metrics', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    # Attach purchase variant rows straight to the base of the order manager sheet
    inlines = [OrderItemInline]

    # ── 4. VISUAL AESTHETIC INTEGRATION SKIN ────────────────────────────────
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)  # Injects your customized teal/gold theme variables
        }