from django.contrib import admin
from .models import ParentProfile
# Register your models here.

@admin.register(ParentProfile)
class ParentProfileAdmin(admin.ModelAdmin):
    list_display = ['surname', 'first_name']
    search_fields = ['surname', 'first_name']