from .views import StaffSignup, StudentSignUp, login, ParentSignup 
from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('student-signup', StudentSignUp.as_view(), name='student_signup'),
    path('staff-signup', StaffSignup.as_view(), name='staff_signup' ),
    path('login', views.user_login, name='user_login'),
    path('parent_signup', ParentSignup.as_view(), name='parent_signup')

]
