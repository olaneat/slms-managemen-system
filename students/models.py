from django.db import models
from .constants import GENDER, BLOOD_GROUP, CLASSESS, CLASS_NAME, TERMS
from register.models import UserRole
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(UserRole, on_delete=models.CASCADE)
    surname = models.CharField(max_length= 50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=50, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    admission_year = models.CharField(max_length=10)
    class_name = models.CharField(choices=CLASS_NAME, max_length=10)
    gender = models.CharField(choices=GENDER, max_length=10)
    student_id = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='img/student',null=True,  blank=True)
    date_of_birth = models.DateField( auto_now=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=15)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    state_of_origin = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ('-surname', 'first_name',)
    
    def __str__(self):
        full_name =  '%s, %s' % (self.surname, self.first_name)
        return full_name
    

@receiver(post_save, sender=UserRole)
def update_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class StudentClass(models.Model):
    student_class = models.CharField(max_length=15, choices=CLASSESS)
    class_name = models.CharField(max_length=15, choices=CLASS_NAME)
    
    class Meta:
        ordering = ('class_name',)

    def __str__(self):
        return self.student_class
     

class SchoolFee(models.Model):
    first_name = models.CharField(max_length=200)
    surname =models.CharField(max_length=200)
    student_class = models.CharField(choices=CLASS_NAME, max_length=10)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    term = models.CharField(choices=TERMS, max_length=15)
    payment_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-student_class', '-surname')
        verbose_name = 'School Fee'
        verbose_name_plural = 'School Fees'
    
    def __str__(self):
        return '%s %s' % (self.surname, self.first_name)
    
class Fees(models.Model):
        fees = models.DecimalField(decimal_places=2, max_digits=9, )
        