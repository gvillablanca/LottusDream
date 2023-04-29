from django import forms
from .models import Cotizacion, Usuario

class CotizacionForm(forms.ModelForm):
    class Meta:
        model =  Cotizacion
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model =  Usuario
        fields = '__all__'