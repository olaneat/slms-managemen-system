from django import forms
from .models import Checkout

QUNATITY_COUNT = [(i, str(i)) for i in range(1, 51)]

class QuantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUNATITY_COUNT, coerce=int)
    update = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=False)

    
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'
        