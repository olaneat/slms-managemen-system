from .models import UserProfile, SchoolFee
from django import forms


class StudentProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(help_text='form of yyyy-mm-dd')
    
    class Meta:
        model = UserProfile
        exclude = ('user',)
        

class SchoolFeeForm(forms.ModelForm):
    class Meta:
        model = SchoolFee
        exclude = ('fees',)

