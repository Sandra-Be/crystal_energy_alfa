from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import UserProfile
from products.models import Product

from django.contrib import messages
from .models import Wishlist

# Create your views here.

def wishlist(request):
    """ A view that renders the wishlist contents page """

    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, product_id):
    """
    Add a product from the store to the
    wishlist
    """

    product = get_object_or_404(Product, pk=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.info(request, 'A new product was added to your wishlist')

    return redirect(redirect_url)