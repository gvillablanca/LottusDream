from django.db import models
from django.contrib.auth.models import User

opciones_evento = [
    [1, "CUMPLEAÑOS"],
    [2, "BODA"],
    [3, "EVENTO SOCIAL"],
    [4, "EVENTO EMPRESA"]
    ]

opciones_salon = [
    [1, "ANDROMEDA"],
    [2, "CASIOPEA"],
    [3, "ORIÓN"],
    [4, "DORADO"],
    [5, "LOTO"]
]

class Cotizacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    correo = models.EmailField()
    telefono = models.CharField(max_length=12)
    cant_personas = models.IntegerField()
    hora_inicio = models.CharField(max_length=20)
    hora_fin = models.CharField(max_length=20)
    fecha = models.CharField(max_length=12)
    id_evento = models.IntegerField(choices=opciones_evento)
    detalle = models.TextField(max_length=150)
    id_salon = models.IntegerField(choices=opciones_salon)

    class Meta:
        managed = False
        db_table = 'cotizacion'
    
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, verbose_name='Rut')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    apellido = models.CharField(max_length=60, verbose_name='Apellido')
    correo = models.CharField(max_length=60, verbose_name='Correo')
    clave = models.CharField(max_length=60, verbose_name='Clave')
    fecha_nac = models.CharField(max_length=12, verbose_name='Fecha de nacimiento (dd-mm-yyyy)')
    fono = models.IntegerField(verbose_name='Fono')
    cargo = models.CharField(max_length=60, verbose_name='cargo del administrador', default='N/A')
    oficina = models.CharField(max_length=60, verbose_name='oficina del administrador', default='N/A')
    tipo = models.CharField(max_length=60, verbose_name='tipo de usuario', default='USUARIO')

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nombre

    
class Evento(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id cotizacion')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    cant_personas = models.IntegerField(verbose_name='cantidad personas')

    class Meta:
        managed = False
        db_table = 'evento'

    def __str__(self):
        return self.nombre
        

class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    representante = models.CharField(max_length=60, verbose_name='Nombre representante')
    direccion = models.CharField(max_length=60, verbose_name='direccion')
    tipo = models.CharField(max_length=60, verbose_name='tipo proveedor')
    detalle = models.CharField(max_length=60, verbose_name='detalle')

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre
    

class Salon(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    estado = models.CharField(max_length=60, verbose_name='Estado')
    ubicacion = models.CharField(max_length=60, verbose_name='Direccion del salon')
    comuna = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'salon'

    def __str__(self):
        return self.nombre
    

class Servicio(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    descripcion = models.CharField(max_length=60, verbose_name='descripcion')
    id_evento = models.IntegerField(verbose_name='id evento')
    id_salon = models.IntegerField(verbose_name='id salon')
    
    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        return self.nombre
