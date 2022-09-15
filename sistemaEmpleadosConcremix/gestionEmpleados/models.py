from django.db import models

class Empleados(models.Model):
    apellido_nombre=models.CharField(max_length=255)
    foto=models.ImageField()
    fecha_nac=models.DateField() # 'aaaa-mm-dd'
    dni=models.CharField(max_length=20)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()
    direccion=models.CharField(max_length=255)
    puesto=models.CharField(max_length=50)
    vehiculo=models.CharField(max_length=100)
    recinto=models.CharField(max_length=100)
    def __str__(self):
        return 'El empleado es: %s, dni: %s, telefono: %s, correo: %s, puesto: %s, recinto: %s'%(self.apellido_nombre,self.dni,self.telefono,self.correo,self.puesto,self.recinto)

class Vehiculos(models.Model):
    nombre_vehiculo=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    modelo=models.IntegerField()
    interno=models.IntegerField()

class Recintos(models.Model):
    nombre_recinto=models.CharField(max_length=100)
    