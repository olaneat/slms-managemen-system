from django.db import models
from .constants import GENDER, BLOOD_GROUP, CLASSESS, CLASS_NAME
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserRole(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_master = models.BooleanField(default=False)

    