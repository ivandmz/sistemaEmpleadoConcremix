from django.contrib import admin
from django.urls import path
from gestionEmpleados import views

urlpatterns=[
    path('',views.planilla_empleados,name="Empleados"),
    path('busqueda/',views.busqueda_empleados,name="Busqueda empleados"),
    path('busqueda/buscar_empleado/',views.buscar_empleado,name="Buscar empleado"),
    path('crear/',views.crear_empleado,name="Nuevo empleado"),
    path('crear/crear_empleado',views.crear_empleado,name="Ingresar empleado"),
    path('editar/<int:id>/',views.editar_empleado,name="Editar empleado"),
    path('alta_baja/<int:id>/',views.alta_baja,name="Alta_baja"),
]