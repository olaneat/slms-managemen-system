from django import forms
from .models import Assignment, SubmitAssignment

class GiveAssignemtForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('topic', 'question', 'student_class', 'deadline', 'subject')


class SubmitAssignemtForm(forms.ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ('answer',)
        

