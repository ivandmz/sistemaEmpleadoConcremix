from django import forms
from gestionEmpleados.models import Vehiculo, Sector

class FormuCrearEmpleado(forms.Form):
    apellido_nombre=forms.CharField()
    foto=forms.ImageField(required=False)
    fecha_nac=forms.DateField()
    dni=forms.CharField()
    telefono=forms.CharField()
    correo=forms.EmailField()
    direccion=forms.CharField()
    fecha_ingreso=forms.DateField()
    fecha_baja=forms.DateField(required=False)
    puesto=forms.CharField()
    vehiculo=forms.CharField(required=False)
    recinto=forms.CharField(required=False)
    activo=forms.BooleanField(required=False)

class FormuCrearVehiculo(forms.ModelForm):
    nombre_vehiculo=forms.CharField(max_length=100)
    marca=forms.CharField(max_length=100)
    modelo=forms.IntegerField()
    interno=forms.IntegerField()
    class Meta:
        model = Vehiculo
        fields = '__all__'

class FormuCrearSector(forms.ModelForm):
    nombre_sector=forms.CharField()
    class Meta:
        model = Sector
        fields = '__all__'