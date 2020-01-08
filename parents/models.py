from django.db import models
from django.dispatch import receiver
from .constants import GENDER, TITLE
from register.models import UserRole
from django.db.models.signals import post_save
# Create your models here.

class ParentProfile(models.Model):
    user = models.OneToOneField(UserRole, on_delete=models.CASCADE)
    title = models.CharField(choices=TITLE, max_length=15)
    surname = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    profile_piture = models.ImageField(upload_to='img/parent', blank=True, null=True)
    first_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    state_of_origin = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=10)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s %s' %(self.surname, self.first_name)
    
    class meta:
        ordering = ('-surname',)
        verbose_name = 'Parent Profile'
        verbose_name_plural = 'Parents Profile'


@receiver(post_save, sender=UserRole)
def update_profile(sender, instance, created, **kwargs):
    if created:
        ParentProfile.objects.create(user=instance)
    instance.parentprofile.save()
            
