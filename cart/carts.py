from shop.models import Item
from django.conf import settings
from decimal import Decimal


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add_item(self, item, quantity=1, update_quantity=False):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0,
                        'price': str(item.price)}


        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
           self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
      self.session.modified = True
      return self.cart


    def remove_item(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()


    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item'] = item

        for value in cart.values():
            value['price'] = Decimal(value['price'])
            value['total_price'] = value['price'] * value['quantity']
            yield value 
    
    
    def __len__(self):
        return sum(value['quantity'] for value in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(value['price']) * value['quantity'] for value in self.cart.values())
    
    def clear_session(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    