from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.planilla_empleados,name="Empleados"),
    path('busqueda/',views.busqueda_empleados,name="Busqueda empleados"),
    path('busqueda/buscar_empleado/',views.buscar_empleado,name="Buscar empleado"),
    path('crear/',views.crear_empleado,name="Nuevo empleado"),
    path('editar/<int:id>/',views.editar_empleado,name="Editar empleado"),
    path('alta_baja/<int:id>/',views.alta_baja,name="Alta_baja"),
    path('vehiculos/',views.planilla_vehiculos, name="Vehiculos"),
    path('vehiculos/busqueda/',views.busqueda_vehiculos,name="Busqueda vehiculos"),
    path('vehiculos/crear/',views.crear_vehiculo,name="Nuevo vehiculo"),
    path('vehiculos/editar/<int:id>/',views.editar_vehiculo,name="Editar vehiculo"),
    path('destruir/<int:id>/',views.destruir,name="Destruir"),



]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)