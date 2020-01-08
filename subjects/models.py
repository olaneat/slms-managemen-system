from django.db import models
from staffs.models import StaffProfile
from django.shortcuts import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from .constants import CLASS_NAME, CLASSESS, TERMS



class Subject(models.Model):
    name = models.CharField(max_length=20)
    subject_teacher = models.CharField(max_length=150)
    staff_id = models.CharField(max_length=20)
    current_term = models.CharField(max_length=15, choices=TERMS)
    student_class = models.CharField(choices=CLASSESS, max_length=20)
    def __str__(self):
        return self.name
            
    class Meta:
        ordering = ('-name',)
        verbose_name = ('Subject')
        verbose_name_plural = ('Subjects')



class SubmitAssignment(models.Model):
    full_name = models.CharField(max_length=250 )
    question = models.ForeignKey('Assignment', blank=True, null=True, related_name='answers', on_delete=models.CASCADE)
    answer = models.FileField(upload_to='assignments')

    class Meta:
        ordering = ('-question',)
        verbose_name = 'Submit Assignment'
        verbose_name_plural = 'Submit Assignments'

    def __str__(self):
        return self.full_name

class Assignment(models.Model):
    topic = models.CharField(max_length= 150, blank=True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    question = models.TextField()
    student_class = models.CharField(choices=CLASS_NAME, max_length=20)
    deadline = models.DateField()

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ('-student_class',)
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'


    def get_absolute_url(self):
        return reverse("students:submit_assignment", args=[self.id])

