from .models import ParentProfile
from django import forms

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        exclude = ('user',)