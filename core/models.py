from django.db import models

class Administrador(models.Model):
    rut_admin = models.CharField(primary_key=True, max_length=60, verbose_name='Rut del administrador')
    nombre = models.CharField(max_length=60, verbose_name='Nombre del administrador')
    apellido = models.CharField(max_length=60, verbose_name='Nombre del administrador')
    correo = models.CharField(max_length=60, verbose_name='Nombre del administrador')
    cargo = models.CharField(max_length=60, verbose_name='Nombre del administrador')
    oficina = models.CharField(max_length=60, verbose_name='Nombre del administrador')

    class Meta:
        managed = False
        db_table = 'administrador'

    def __str__(self):
        print(self.nombre)
        return self.nombre


