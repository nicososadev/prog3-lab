from django import forms

from .models import Mensaje

class ContactFrom(forms.ModelForm):

    class Meta:
        model = Mensaje
        fields = (
            'name',
            'email',
            'content'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    