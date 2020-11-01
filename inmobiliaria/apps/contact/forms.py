from django import forms

from .models import Mensaje

class ContactFrom(forms.ModelForm):

    # forms.Form -----

    # name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
    #     attrs={'class':'form-control'}
    # ))
    # email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
    #     attrs={'class':'form-control'}
    # ))
    # content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
    #     attrs={'class':'form-control'}
    # ))


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
    