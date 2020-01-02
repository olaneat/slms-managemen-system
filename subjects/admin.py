from django.contrib import admin
from .models import Assignment, Subject 
# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name' ]

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['question', 'subject']
    search_fields = ['title', 'question', 'subject']
