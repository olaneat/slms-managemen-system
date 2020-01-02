from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, blank =True)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=False)
    img = models.ImageField(upload_to='img/shop')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


    def get_absolute_url(self):
        return reverse("shop:item_detail", args=[self.id, self.slug ])
    
class Category(models.Model):
    category = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    
    def get_absolute_url(self):
        return reverse("shop:category_list", args=[self.slug])

    def __str__(self):
        return self.category
        
    class Meta:
        ordering = ('-category',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    