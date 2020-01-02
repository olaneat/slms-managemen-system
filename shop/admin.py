from django.contrib import admin
from .models import Item, Category
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    prepopulated_fields = {'slug': ('category',)}
    search_fields = ['category']

