from django.db import models
from subjects.models import Subject
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import UserProfile
from .constants import TERMS, GRADES
# Create your models here.

class StudentResult(models.Model):
    name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    term = models.CharField(choices=TERMS, max_length=15)
    subjects = models.ForeignKey('SubjectGrade', on_delete=models.CASCADE )

class SubjectGrade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ca_score = models.DecimalField(max_digits=9, decimal_places=2)
    exam_score = models.DecimalField(max_digits=9, decimal_places=2)
    total_score =models.DecimalField(max_digits=9, decimal_places=2)
    grade = models.CharField(choices=GRADES, max_length=5)