from django.contrib import admin
from .models import PortfolioItem

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    # Swapped 'category' for our dynamic string converter method
    list_display = ('title', 'display_categories', 'created_at')
    list_filter = ('categories',)
    search_fields = ('title',)

    def display_categories(self, obj):
        return ", ".join([c.get_code_display() for c in obj.categories.all()])
    display_categories.short_description = 'Categories'