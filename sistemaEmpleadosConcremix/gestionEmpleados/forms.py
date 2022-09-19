from django import forms

class FormuCrearEmpleado(forms.Form):
    apellido_nombre=forms.CharField()
    foto=forms.ImageField()
    fecha_nac=forms.DateField()
    dni=forms.CharField()
    telefono=forms.CharField()
    correo=forms.EmailField()
    direccion=forms.CharField()
    fecha_ingreso=forms.DateField()
    fecha_baja=forms.DateField()
    puesto=forms.CharField()
    vehiculo=forms.CharField()
    recinto=forms.CharField()
    activo=forms.BooleanField()