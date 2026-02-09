from django import forms 
from .models import BinaryVarity


class BinaryVarityForm(forms.Form):
    binary_varity = forms.ModelChoiceField(queryset=BinaryVarity.objects.all(), label="Select binary variety")

    # for example :
    # binary_varity = forms.CharField()
    