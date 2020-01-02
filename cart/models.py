from django.db import models
from students.models import StudentClass
# Create your models here.
class Checkout(models.Model):
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    student_class = models.OneToOneField(StudentClass, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True,null=True)

    class Meta:
        ordering = ('surname', 'student_class',)
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'
    
    def __str__(self):
        return self.first_name
    
    
