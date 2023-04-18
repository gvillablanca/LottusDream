from django.db import models

class Administrador(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id del administrador')
    rut = models.IntegerField(verbose_name='rut del administrador')
    dv = models.CharField(max_length=1, verbose_name='dv del administrador')
    nombre = models.CharField(max_length=20, verbose_name='Nombre del administrador')
    apellido = models.CharField(max_length=20, verbose_name='apellido del administrador')
    correo = models.CharField(max_length=20, verbose_name='correo del administrador')
    oficina = models.CharField(max_length=20, verbose_name='oficina del administrador')
    clave = models.CharField(max_length=20, verbose_name='clave del administrador')

    class Meta:
        managed = False
        db_table = 'administrador'


class Cliente(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    rut = models.IntegerField(verbose_name='rut')
    dv = models.CharField(max_length=1, verbose_name='dv')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='apellido')
    correo = models.CharField(max_length=20, verbose_name='correo')
    clave = models.CharField(max_length=20, verbose_name='clave')


    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.nombre
    
    
class Cotizacion(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')
    class Meta:
        managed = False
        db_table = 'cotizacion'

    def __str__(self):
        return self.nombre
    
    
class Evento(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')

    class Meta:
        managed = False
        db_table = 'evento'

    def __str__(self):
        return self.nombre
        

class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre
    
class Salon(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')

    class Meta:
        managed = False
        db_table = 'salon'

    def __str__(self):
        return self.nombre
    

class Servicio_evento(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id')

    class Meta:
        managed = False
        db_table = 'servicio_evento'

    def __str__(self):
        return self.nombre