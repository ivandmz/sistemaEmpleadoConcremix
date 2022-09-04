from django.db import models

class Empleados(models.Model):
    id_empleado=models.IntegerField()
    apellido_nombre=models.CharField(max_length=255)
    foto=models.ImageField()
    fecha_nac=models.DateField()
    dni=models.CharField(max_length=20)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()
    direccion=models.CharField(max_length=255)
    puesto=models.CharField(max_length=50)
    vehiculo=models.CharField(max_length=100)
    recinto=models.CharField(max_length=100)

class Vehiculos(models.Model):
    id_vehiculo=models.IntegerField()
    nombre=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    modelo=models.IntegerField()
    interno=models.IntegerField()

class Recintos(models.Model):
    id_recinto=models.IntegerField()
    