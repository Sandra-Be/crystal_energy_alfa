from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JzpVfCW1CFTqgZWoUbGANLKvDTBW9aD2GdNNONfXNsdJf6rorbJxjU1vZv1tWSpTEJOEMosCmY90jcaHEAF3dw000ZJq726dm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
