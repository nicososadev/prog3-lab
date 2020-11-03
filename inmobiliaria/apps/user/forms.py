from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': "Correo"})
    )
    password = forms.CharField(label='Email', required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder': "Contraseña"})
    )

class RegisterForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': "Nombre"})
    )
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': "Correo"})
    )
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder': "Contraseña"})
    )
    password2 = forms.CharField(label='Confirmar Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder': "Confirmar Contraseña"})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("La dirección correo electrónico ya existe")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]