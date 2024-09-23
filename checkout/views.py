from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q2ANhFfV0GWPjVM0XmO4p78uSVuSyKXWRUMn4ACF7lHT2ROFdBptCNb7PdFizLkZ50fzGS65bdkXgXoC8t52osi00mTEX2EC8',
        'client_secret': 'test client server',
    }

    return render(request, template, context)