# Generated by Django 4.2 on 2023-04-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del administrador')),
                ('rut', models.IntegerField(verbose_name='rut del administrador')),
                ('dv', models.CharField(max_length=1, verbose_name='dv del administrador')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre del administrador')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido del administrador')),
                ('correo', models.CharField(max_length=20, verbose_name='correo del administrador')),
                ('oficina', models.CharField(max_length=20, verbose_name='oficina del administrador')),
                ('clave', models.CharField(max_length=20, verbose_name='clave del administrador')),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('rut', models.IntegerField(verbose_name='rut')),
                ('dv', models.CharField(max_length=1, verbose_name='dv')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido')),
                ('correo', models.CharField(max_length=20, verbose_name='correo')),
                ('clave', models.CharField(max_length=20, verbose_name='clave')),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'cotizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'salon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio_evento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'servicio_evento',
                'managed': False,
            },
        ),
    ]
