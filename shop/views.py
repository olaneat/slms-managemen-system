from django.shortcuts import render, get_object_or_404
from cart.forms import QuantityForm
from .models import Item, Category
# Create your views here.

def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True) 
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = Item.objects.filter(category=category)
    return render(request, 'shop/index.html', {'categories': categories, 'category':category,'items':items})


def item_detail(request, id, slug):
    item = get_object_or_404(Item, 
                            slug=slug, 
                            id=id,
                            available=True)
    quantity_form =QuantityForm()
    return render(request, 'shop/item_detail.html', {'item': item, 'quantity_form': quantity_form})
    
