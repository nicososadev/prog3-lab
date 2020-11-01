from django import forms

from .models import Propiedad ,PROPERTY_TYPE, OPERATION

class PropiedadForm(forms.ModelForm):
    # propType = forms.ChoiceField(label='Tipo Propiedad', required=True, choices=PROPERTY_TYPE, widget=forms.Select(
    #     attrs={'class':'form-control', 'placeholder': "Tipo Propiedad"})
    # )
    # operation = forms.ChoiceField(label='Tipo Operacion', required=True, choices=OPERATION, widget=forms.Select(
    #     attrs={'class':'form-control', 'placeholder': "Tipo Operacion"})
    # )
    # description = forms.CharField(label='Descripcion', required=True, widget=forms.Textarea(
    #     attrs={'class':'form-control', 'placeholder': "Descripcion"})
    # )
    # image = forms.ImageField(label='imagen', required=True)
    # rooms = forms.IntegerField(label='Habitaciones', required=True, widget=forms.NumberInput(
    #     attrs={'class':'form-control', 'placeholder': "Habitaciones"})
    # )
    # bathrooms = forms.IntegerField(label='Baños', required=True, widget=forms.NumberInput(
    #     attrs={'class':'form-control', 'placeholder': "Baños"})
    # )
    # surfice = forms.IntegerField(label='Superficie', required=True, widget=forms.NumberInput(
    #     attrs={'class':'form-control', 'placeholder': "Superficie"})
    # )
    # price = forms.DecimalField(label='Precio', required=True, widget=forms.NumberInput(
    #     attrs={'class':'form-control', 'placeholder': "Precio"})
    # )

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