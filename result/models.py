from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import UserProfile
from subjects.models import Subject
from .constants import TERMS, GRADES, COMMENT, CLASS_NAME
# Create your models here.

class Student(models.Model):
    name = models.OneToOneField(UserProfile, on_delete = models.CASCADE)
    student_reg_no = models.CharField(max_length=20, blank=True, null=True)
    student_class = models.CharField(choices=CLASS_NAME, max_length=20)
    
    def __str__(self):
        return '%s %s' %(self.name.surname, self.name.first_name)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Student'
        verbose_name_plural = 'Students '

    
class Session(models.Model):
    session = models.CharField(max_length=150)
    is_current_session = models.BooleanField(default=False)
    next_session_begins = models.DateField(null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.session

    class Meta:
        ordering = ('session',)
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'


class Term(models.Model):
    term = models.CharField(max_length=20, choices=TERMS)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    current_term = models.BooleanField(default=False, blank=True, null=True)
    next_term_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        ordering = ('-term',)
        verbose_name = 'Term'
        verbose_name_plural = 'Terms'


class Result(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20, )
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete = models.CASCADE )
    position = models.CharField(max_length=10)
    average = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(choices=GRADES, max_length=15)
    comment = models.CharField(choices=COMMENT, max_length=20)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Resut'
        verbose_name_plural = 'Result'


class SubjectOffered(models.Model):
    full_name = models.CharField(max_length=150)
    student_class = models.CharField(choices=CLASS_NAME, max_length=15)
    student_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    ca_score = models.PositiveIntegerField(blank=True, null=True, default=0)
    exam_score = models.PositiveIntegerField(blank=True, null=True, default=0)
    total_score =models.PositiveIntegerField(blank=True, null=True, default=0)
    grade = models.CharField(choices=GRADES, max_length=5)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ('-term', '-session', '-full_name')
        verbose_name = 'Subject Offered'
        verbose_name_plural = 'Subjects Offered'

    
    