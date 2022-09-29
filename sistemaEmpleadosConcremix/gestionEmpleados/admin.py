from django.contrib import admin
from gestionEmpleados.models import Empleado,Vehiculo,Sector

class EmpleadoAdmin(admin.ModelAdmin):
    if Empleado.activo == False:
        list_display = ("apellido_nombre","foto","fecha_nac","dni","telefono","correo","direccion","fecha_ingreso","puesto","vehiculo","recinto","activo","fecha_baja",)
    else:
        list_display = ("apellido_nombre","foto","fecha_nac","dni","telefono","correo","direccion","fecha_ingreso","puesto","vehiculo","recinto","activo",)
    search_fields = ("apellido_nombre","dni","puesto","vehiculo","recinto",)
    list_filter = ("puesto","vehiculo","recinto",)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("nombre_vehiculo","marca","modelo","interno",)
    search_fields = ("interno","modelo",)
    list_filter = ("modelo","marca",)

class SectorAdmin(admin.ModelAdmin):
    list_display = ("nombre_sector",) # si tiene un solo item debe agregar la coma al final para q lo considere tupla
    search_fields = ("nombre_sector",)

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Sector,SectorAdmin)