from xml.dom import ValidationErr
from django import forms
from traitlets import ValidateHandler
from .models import Vehicle, Registration
from datetime import date
from django.utils.translation import gettext_lazy as _

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('id',)
        widgets = {'first_registration':forms.widgets.DateInput(attrs=  {'type':'date'})

        }

class RegistrationForm(forms.ModelForm):
    
    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        start_date = self.cleaned_data.get('start_date')
        if end_date is not None and start_date is not None:
            if end_date < start_date:
                raise forms.ValidationError(_('Deregistration cannot be done before registration'))

    class Meta:
        model = Registration
        fields = ('plate', 'start_date', 'end_date', 'active')
        widgets = {
            'start_date':forms.widgets.DateInput(attrs={'type':'date'}),
            'end_date':forms.widgets.DateInput(attrs={'type':'date'})
        }
        

class VehicleDeleteConfirmForm(forms.Form):
        items = forms.CharField(disabled=True)







