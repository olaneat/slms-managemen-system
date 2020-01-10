from django.contrib import admin
from .models import Session, Term, SubjectOffered, Student, Result
# Register your models here.

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ['term', 'session']
    search_fields = ['term']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session']
    search_fields = ['session']



@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'term', 'session']
    search_fields = ('full_name', 'student_number')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_class']

@admin.register(SubjectOffered)
class SubjectOfferedAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'student_number', 'session', 'term']
    search_fields = ['full_name', 'student_number']