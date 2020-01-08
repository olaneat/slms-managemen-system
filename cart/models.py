from django.db import models
from .constants import CLASS_NAME
# Create your models here.
class Checkout(models.Model):
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    student_class = models.CharField(max_length=15, choices=CLASS_NAME)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True,null=True)

    class Meta:
        ordering = ('surname', 'student_class',)
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'
    
    def __str__(self):
        return '%s %s' %(self.surname, self.first_name)

    
    
