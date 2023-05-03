from .models import Cotizacion, Salon, Usuario, Proveedor, Servicio, Evento
from rest_framework import serializers

class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Cotizacion
        fields = '__all__'

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Salon
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Usuario
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Proveedor
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Servicio
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Evento
        fields = '__all__'
