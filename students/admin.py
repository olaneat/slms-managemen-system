from django.contrib import admin
from .models import UserProfile , StudentClass, SchoolFee

@admin.register(UserProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'student_id', 'class_name']
    search_fields = ('surname', 'first_name', 'student_id')

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'student_class']

@admin.register(SchoolFee)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['surname', 'first_name', 'student_class']
    search_fields = ['student_class', 'surname']
    