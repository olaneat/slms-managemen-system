from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/<int:year>/<int:month>/<int:day>', views.post_detail, name='post_detail'),
]
