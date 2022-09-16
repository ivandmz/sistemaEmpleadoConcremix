from django.db import models

class Empleados(models.Model):
    apellido_nombre=models.CharField(max_length=255,verbose_name="Nombre completo")
    foto=models.ImageField(blank=True,null=True)
    fecha_nac=models.DateField(verbose_name="Fecha nacimiento") # 'aaaa-mm-dd'
    dni=models.CharField(max_length=20,verbose_name="DNI")
    telefono=models.CharField(max_length=20)
    correo=models.EmailField(blank=True,null=True)
    direccion=models.CharField(max_length=255)
    fecha_ingreso=models.DateField(verbose_name="Fecha ingreso")
    fecha_baja=models.DateField(verbose_name="Fecha baja",blank=True,null=True)
    puesto=models.CharField(max_length=50)
    vehiculo=models.CharField(max_length=100,blank=True,null=True)
    recinto=models.CharField(max_length=100,blank=True,null=True)
    activo=models.BooleanField(default=True)
    def __str__(self):
        return 'El empleado es: %s, dni: %s, telefono: %s, correo: %s,fecha ingreso: %s, puesto: %s, recinto: %s'%(self.apellido_nombre,self.dni,self.telefono,self.correo,self.fecha_ingreso,self.puesto,self.recinto)

class Vehiculos(models.Model):
    nombre_vehiculo=models.CharField(max_length=100,verbose_name="Nombre vehiculo")
    marca=models.CharField(max_length=100)
    modelo=models.IntegerField()
    interno=models.IntegerField()

class Recintos(models.Model):
    nombre_recinto=models.CharField(max_length=100,verbose_name="Sector")
    