from .views import StaffSignUp, StudentSignUp, login, ParentSignUp, ClassMasterSignUp
from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('student-signup', StudentSignUp.as_view(), name='student_signup'),
    path('staff-signup', StaffSignUp.as_view(), name='staff_signup' ),
    path('login', views.user_login, name='user_login'),
    path('parent_signup', ParentSignUp.as_view(), name='parent_signup'),
    path('staff-signup', ClassMasterSignUp.as_view(), name='class_master_signup' )

]
