from django import forms
from .models import Document
from searchableselect.widgets import SearchableSelect


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')
        #widgets = {
        #    'vehicle': SearchableSelect(model='vehicle.Vehicle', search_field='plate', limit=10)
        #}

class DeleteForm(forms.Form):
        items = forms.CharField(disabled=True)