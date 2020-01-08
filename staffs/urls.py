from . import views
from django.urls import path

app_name = 'staffs'

urlpatterns = [
    
    path('', views.staff_index, name='staff_index'),
    path('edit_profile', views.edit_profile, name='profile'),
    path('give_assignment', views.give_assignment, name='give_assignment'),
]
