from django.db import models

class Category(models.Model):
    CODE_CHOICES = [
        ('fan_art', 'Fan Art'),
        ('original', 'Original'),
        ('dark_art', 'Dark Art'),
        ('portrait', 'Portrait'),
    ]
    code = models.CharField(max_length=20, choices=CODE_CHOICES, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.get_code_display()

class ShopItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop_images/')
    # Swapped from CharField to ManyToManyField
    categories = models.ManyToManyField(Category, related_name='shop_items')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Base price in GHC")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ItemFormat(models.Model):
    shop_item = models.ForeignKey(ShopItem, on_delete=models.CASCADE, related_name='formats')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price for this specific format in GHC")

    def __str__(self):
        return f"{self.name} ({self.price} GHC) - {self.shop_item.title}"