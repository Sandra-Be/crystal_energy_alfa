from django.db import models
from profiles.models import UserProfile
from products.models import Product

# Create your models here.


class Wishlist(models.Model):
    """
    Model to show all product items within the users wishlist
    """
    user = models.OneToOneField(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist')

    def __str__(self):
        return f'Wishlist, ({self.user})'


class WishlistItem(models.Model):
    """
    A model, allowing users to add
    individual products to their wishlist.
    """

    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_products')
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_items')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
