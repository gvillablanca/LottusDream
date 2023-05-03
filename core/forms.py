from django import forms
from .models import Cotizacion, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CotizacionForm(forms.ModelForm):
    class Meta:
        model =  Cotizacion
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model =  Usuario
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
