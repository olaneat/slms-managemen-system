from django.contrib import admin
from .models import Checkout 
# Register your models here.

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'student_class']
    search_fields = ['surname', 'student_class']
    