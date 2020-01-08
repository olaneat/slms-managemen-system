from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Item
from .carts import Cart
from .forms import QuantityForm, CheckoutForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_POST
def add_to_cart(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    quantity_form = QuantityForm(request.POST)
    if quantity_form.is_valid():
        cd = quantity_form.cleaned_data
        cart.add_item(item = item,
                        quantity=cd['quantity'],
                        update_quantity= cd['update']       
        )
    return redirect('cart:cart_detail')

@login_required
def delete_item(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove_item(item)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        checkout_form  = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            cd = checkout_form.cleaned_data
            cd.save()
            return render(request, 'cart:payment.html', {'email':cd.email, 'cart':cart})
        else:
            return HttpResponse('Check the information, correct the errors and try again')
    else:
        checkout_form = CheckoutForm()
    return render(request, 'cart/checkout_form.html', {'checkout_form': checkout_form})