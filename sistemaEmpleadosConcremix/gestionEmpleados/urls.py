from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.planilla_empleados,name="Empleados"),
    path('busqueda/',views.busqueda_empleados,name="Busqueda empleados"),
    path('crear/',views.crear_empleado,name="Nuevo empleado"),
    path('editar/<int:id>/',views.editar_empleado,name="Editar empleado"),
    path('alta_baja/<int:id>/',views.alta_baja,name="Alta_baja"),
    path('vehiculos/',views.planilla_vehiculos, name="Vehiculos"),
    path('vehiculos/busqueda/',views.busqueda_vehiculos,name="Busqueda vehiculos"),
    path('vehiculos/crear/',views.crear_vehiculo,name="Nuevo vehiculo"),
    path('vehiculos/editar/<int:id>/',views.editar_vehiculo,name="Editar vehiculo"),
    path('vehiculos/destruir/<int:id>/',views.eliminar_vehiculo,name="Destruir"),
    path('sectores/',views.planilla_sectores, name="Sectores"),
    path('sectores/busqueda/',views.busqueda_sectores,name="Busqueda sectores"),
    path('sectores/crear/',views.crear_sector,name="Crear sector"),
    path('sectores/editar/<int:id>/',views.editar_sector,name="Editar sector"),
    path('sectores/destruir/<int:id>/',views.eliminar_sector,name="Destruir sector"),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)