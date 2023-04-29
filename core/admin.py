from django.contrib import admin
from .models import Usuario, Cotizacion, Evento, Proveedor, Salon, Servicio

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Proveedor)
admin.site.register(Salon)
admin.site.register(Servicio)
admin.site.register(Cotizacion)