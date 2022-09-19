from django.contrib import admin
from django.urls import path
from gestionEmpleados import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.planilla_empleados,name="Empleados"),
    path('busqueda/',views.busqueda_empleados,name="Busqueda empleados"),
    path('buscar/',views.buscar_empleado,name="Buscar empleado"),
    path('crear/',views.crear_empleado,name="Ingresar empleado"),
]