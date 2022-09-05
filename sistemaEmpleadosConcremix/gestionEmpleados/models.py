from django.db import models

class Empleados(models.Model):
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
    nombre_vehiculo=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    modelo=models.IntegerField()
    interno=models.IntegerField()

class Recintos(models.Model):
    nombre_recinto=models.CharField(max_length=100)
    