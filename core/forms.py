from .models import *
from django import forms
from django.forms.widgets import DateInput, Select 

class HoppsForm(forms.ModelForm):
  

    class Meta:
        model = Hopps
        fields = [ 'first_name', 'last_name', 'equip_type', 'description', 'office', 'staff' ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'style': 'margin-bottom: 10px'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'equip_type': Select(attrs={'class': 'form-control','style': 'margin-bottom: 10px'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'office': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'description': '',
        }

        