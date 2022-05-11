from django import forms
from .models import Vehicle, Registration

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('id',)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('plate', 'start_date', 'end_date')

class VehicleDeleteConfirmForm(forms.Form):
        items = forms.CharField(disabled=True)







