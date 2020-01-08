from . import views
from django.urls import path


app_name = 'parents'
urlpatterns = [
    path('create_profile', views.create_profile, name='create_profile'),
    path('', views.index, name='index')
    
]
