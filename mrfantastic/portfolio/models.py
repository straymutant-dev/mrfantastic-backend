from django.db import models
from shop.models import Category # Import our updated category model

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio_images/')
    # Swapped from CharField to ManyToManyField
    categories = models.ManyToManyField(Category, related_name='portfolio_items')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title