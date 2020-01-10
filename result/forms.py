from .models import *
from django import forms

class SubjectOfferedForm(forms.ModelForm):
    class Meta:
        model = SubjectOffered
        fields = '__all__'


class ResultForm(forms.ModelForm):
    models = Result
    fields = '__all__'
    
