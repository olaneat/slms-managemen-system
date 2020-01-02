from django.contrib import admin
from .models import StaffProfile
# Register your models here.

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ['surname', 'first_name', 'staff_id']
    search_fields = ['surname', 'staff_id', 'first_name']