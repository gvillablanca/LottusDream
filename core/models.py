from django.db import models

class Cotizacion(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id cotizacion')
    cant_personas = models.IntegerField(verbose_name='cantidad personas')
    tipo_evento = models.CharField(max_length=60, verbose_name='tipo evento')
    detalle = models.CharField(max_length=60, verbose_name='detalle')
    estado = models.CharField(max_length=60, verbose_name='estadoo')
    id_usuario = models.IntegerField(verbose_name='id usuario')
    id_evento = models.IntegerField(verbose_name='id evento')
    id_salon = models.IntegerField(verbose_name='id salon')

    class Meta:
        managed = False
        db_table = 'cotizacion'

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    apellido = models.CharField(max_length=60, verbose_name='apellido')
    correo = models.CharField(max_length=60, verbose_name='correo')
    fecha_nac = models.DateField(verbose_name='fecha de nacimiento')
    fono = models.IntegerField(verbose_name='fono')
    cargo = models.CharField(max_length=60, verbose_name='cargo del administrador')
    oficina = models.CharField(max_length=60, verbose_name='oficina del administrador')
    tipo = models.CharField(max_length=60, verbose_name='tipo de usuario')

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nombre
    
    
class Evento(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id cotizacion')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    cant_personas = models.IntegerField(verbose_name='cantidad personas')
    hora_inicio = models.CharField(max_length=20, verbose_name='hora inicio')
    hora_fin = models.CharField(max_length=20, verbose_name='hora fin')
    id_proveedor = models.IntegerField(verbose_name='id proveedor')
    id_evento = models.IntegerField(verbose_name='id evento')
    id_salon = models.IntegerField(verbose_name='id salon')

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

    class Meta:
        managed = False
        db_table = 'salon'

    def __str__(self):
        return self.nombre
    

class Servicio_evento(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    descripcion = models.CharField(max_length=60, verbose_name='descripcion')
    id_evento = models.IntegerField(verbose_name='id evento')
    id_salon = models.IntegerField(verbose_name='id salon')
    
    class Meta:
        managed = False
        db_table = 'servicio_evento'

    def __str__(self):
        return self.nombre