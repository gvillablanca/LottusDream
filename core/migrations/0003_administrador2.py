# Generated by Django 4.2 on 2023-04-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_cliente_delete_cotizacion_delete_evento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador2',
            fields=[
                ('rut_admin', models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='Rut del administrador')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del administrador')),
                ('apellido', models.CharField(max_length=60, verbose_name='Nombre del administrador')),
                ('correo', models.CharField(max_length=60, verbose_name='Nombre del administrador')),
                ('cargo', models.CharField(max_length=60, verbose_name='Nombre del administrador')),
                ('oficina', models.CharField(max_length=60, verbose_name='Nombre del administrador')),
            ],
            options={
                'db_table': 'administrador2',
                'managed': False,
            },
        ),
    ]
