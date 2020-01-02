from . import views
from django.urls import path

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.index, name='category_list'),
    path('item_detail/<int:id>/<slug:slug>', views.item_detail, name='item_detail')
]
