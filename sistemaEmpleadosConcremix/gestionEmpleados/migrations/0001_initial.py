# Generated by Django 4.1 on 2022-09-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empleado', models.IntegerField()),
                ('apellido_nombre', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
                ('fecha_nac', models.DateField()),
                ('dni', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=50)),
                ('vehiculo', models.CharField(max_length=100)),
                ('recinto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recintos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recinto', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
                ('nombre_recinto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vehiculo', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
                ('nombre_vehiculo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.IntegerField()),
                ('interno', models.IntegerField()),
            ],
        ),
    ]
