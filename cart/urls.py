from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<int:item_id>', views.delete_item, name='remove_from_cart' ),
    path('check-out', views.checkout, name='checkout')
]

