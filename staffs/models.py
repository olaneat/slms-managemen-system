from django.db import models
from register.models import UserRole
from .constants import GENDER, BLOOD_GROUP
from django.dispatch import receiver
from django.db.models.signals import post_save 

class StaffProfile(models.Model):
    user = models.OneToOneField(UserRole,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=250 )
    middle_name  = models.CharField(max_length=250, blank=True, null=True)
    surname  = models.CharField(max_length=250)
    gender = models.CharField(max_length=15, choices=GENDER)
    staff_id = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='img/staff', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length= 20, )
    email = models.EmailField(blank=True, null=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP )
    nationality = models.CharField(max_length=150)
    state_of_origin = models.CharField(max_length=150)
    
    class Meta:
        ordering = ('-surname', '-first_name')
        verbose_name = 'Staff Profile'
        verbose_name_plural = 'Staffs Profile'
    
    def __str__(self):
        return '%s %s' %(self.surname, self.first_name)

@receiver(post_save, sender=UserRole)
def update_staff_profile(sender, instance, created, **kwargs):
    if created:
        StaffProfile.objects.create(user=instance)
    instance.staffprofile.save()