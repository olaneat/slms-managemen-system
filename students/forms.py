from .models import UserProfile
from django import forms


class StudentProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(help_text='form of yyyy-mm-dd')
    
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
