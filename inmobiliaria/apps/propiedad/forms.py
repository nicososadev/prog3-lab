from django import forms

from .models import Propiedad ,PROPERTY_TYPE, OPERATION

class PropiedadForm(forms.ModelForm):

    class Meta:
        model = Propiedad
        fields = (
            'propType',
            'operation',
            'description',
            'image',
            'rooms',
            'bathrooms',
            'surfice',
            'price'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'