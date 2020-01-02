from django import forms
from .models import UserRole
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class StudentSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserRole
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

class StaffSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserRole
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length= 150)
    password = forms.CharField(widget=forms.PasswordInput, max_length= 150)
