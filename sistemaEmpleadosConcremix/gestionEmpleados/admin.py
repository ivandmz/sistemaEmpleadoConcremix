from django.contrib import admin
from gestionEmpleados.models import Empleados,Vehiculos,Recintos

class EmpleadosAdmin(admin.ModelAdmin):
    if Empleados.activo == False:
        list_display = ("apellido_nombre","foto","fecha_nac","dni","telefono","correo","direccion","fecha_ingreso","puesto","vehiculo","recinto","activo","fecha_baja",)
    else:
        list_display = ("apellido_nombre","foto","fecha_nac","dni","telefono","correo","direccion","fecha_ingreso","puesto","vehiculo","recinto","activo",)
    search_fields = ("apellido_nombre","dni","puesto","vehiculo","recinto",)
    list_filter = ("puesto","vehiculo","recinto",)

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ("nombre_vehiculo","marca","modelo","interno",)
    search_fields = ("interno","modelo",)
    list_filter = ("modelo","marca",)

class RecintosAdmin(admin.ModelAdmin):
    list_display = ("nombre_recinto",) # si tiene un solo item debe agregar la coma al final para q lo considere tupla
    search_fields = ("nombre_recinto",)

admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Vehiculos,VehiculosAdmin)
admin.site.register(Recintos,RecintosAdmin)