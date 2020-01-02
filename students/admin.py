from django.contrib import admin
from .models import UserProfile , StudentClass

@admin.register(UserProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'student_id', 'class_name']
    search_fields = ('surname', 'first_name', 'student_id')

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'student_class']