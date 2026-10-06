from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import ShopItem, ItemFormat, Category

# Register the Category model so you can manage tags
admin.site.register(Category)

class DefaultFormatsFormSet(BaseInlineFormSet):
    """
    Custom formset to automatically pre-populate the 6 standard 
    buying options whenever a brand-new artwork is added.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Check if this is a brand new item (instance doesn't have a database primary key yet)
        if not self.instance.pk:
            self.initial = [
                {'name': 'Printed Portrait'},
                {'name': 'Phone Cover'},
                {'name': 'Sticker'},
                {'name': 'Canvas Wrap'},
                {'name': 'Framed Print'},
                {'name': 'Tote Bag'}
            ]

class ItemFormatInline(admin.TabularInline):
    model = ItemFormat
    formset = DefaultFormatsFormSet
    extra = 6  # Match the exact number of default choices above
    max_num = 12  # Gives you the flexibility to add extra unique options later if needed

@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_categories', 'base_price', 'is_available', 'created_at')
    list_filter = ('categories', 'is_available')
    search_fields = ('title', 'description')
    inlines = [ItemFormatInline]

    def display_categories(self, obj):
        return ", ".join([c.get_code_display() for c in obj.categories.all()])
    display_categories.short_description = 'Categories'