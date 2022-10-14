from django.db import models

class Vehiculo(models.Model):
    nombre_vehiculo=models.CharField(max_length=100,verbose_name="Nombre vehiculo")
    marca=models.CharField(max_length=100)
    modelo=models.IntegerField()
    interno=models.IntegerField()
    class Meta:
        verbose_name='vehiculo'
        verbose_name_plural='vehiculos'
    def __str__(self) -> str:
        return 'interno %s: %s'%(self.interno,self.nombre_vehiculo)

class Sector(models.Model):
    nombre_sector=models.CharField(max_length=100,verbose_name="Sector")
    class Meta:
        verbose_name='sector'
        verbose_name_plural='sectores'
    def __str__(self):
        return '%s'%(self.nombre_sector)

class Empleado(models.Model):
    apellido_nombre=models.CharField(max_length=255,verbose_name="Nombre completo")
    foto=models.ImageField(upload_to="empleados",blank=True,null=True)
    fecha_nac=models.DateField(verbose_name="Fecha nacimiento") # 'aaaa-mm-dd'
    dni=models.CharField(max_length=20,verbose_name="DNI")
    telefono=models.CharField(max_length=20)
    correo=models.EmailField(blank=True,null=True)
    direccion=models.CharField(max_length=255)
    fecha_ingreso=models.DateField(verbose_name="Fecha ingreso")
    fecha_baja=models.DateField(verbose_name="Fecha baja",blank=True,null=True)
    puesto=models.CharField(max_length=50)
    vehiculo=models.ForeignKey(Vehiculo,blank=True,null=True,on_delete=models.SET_NULL)
    sector=models.ForeignKey(Sector,blank=True,null=True,on_delete=models.SET_NULL)
    activo=models.BooleanField(default=True)
    class Meta:
        verbose_name='empleado'
        verbose_name_plural='empleados'
    def __str__(self):
        cadena =  'El empleado es: %s, dni: %s, telefono: %s, correo: %s,fecha ingreso: %s, puesto: %s'%(self.apellido_nombre,self.dni,self.telefono,self.correo,self.fecha_ingreso,self.puesto)
        if self.sector:
            cadena+=', sector: %s'%(self.sector) # debería hacer la misma validación con cada item...
        if self.vehiculo:
            cadena+=', vehículo: %s'%(self.vehiculo)
        cadena +='.'
        return cadena
    