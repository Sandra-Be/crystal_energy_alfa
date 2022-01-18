from django.db import models
from django.contrib.auth.models import User
from .models import Product


class Review(models.Model):
    """ Model for reviews """
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 null=True, blank=True)
    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254, null=True, blank=True)
    body = models.CharField(max_length=1000)
    firstcreated = models.DateTimeField(auto_now_add=True)
    lasteditted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)
