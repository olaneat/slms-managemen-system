from . import views
from django.urls import path

app_name = 'students'
urlpatterns = [
    path('', views.student_index, name='index'),
    path('edit_profile', views.edit_profile, name='profile'),
    path('submit_assignment/<int:id>', views.submit_assignment, name='submit_assignment')

]
