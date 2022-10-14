from datetime import date
from django import forms
from gestionEmpleados.models import Empleado, Vehiculo, Sector


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
    vehiculo=forms.IntegerField(required=False)
    sector=forms.IntegerField(required=False)
    activo=forms.BooleanField(required=False)

class FormuEditarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'fecha_nac': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
            'fecha_ingreso': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
            'fecha_baja': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
        }

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