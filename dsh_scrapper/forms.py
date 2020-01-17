from django import forms

from .models import Client

class AddClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddClientForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Client
        fields = ('name', 'url',)