from django import forms
from .models import Vehicle, Registration


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('id',)
        widgets = {'first_registration':forms.widgets.DateInput(attrs=  {'type':'date'})

        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('plate', 'start_date', 'end_date')
        widgets = {
            'start_date':forms.widgets.DateInput(attrs={'type':'date'}),
            'end_date':forms.widgets.DateInput(attrs={'type':'date'})
        }
        

class VehicleDeleteConfirmForm(forms.Form):
        items = forms.CharField(disabled=True)







