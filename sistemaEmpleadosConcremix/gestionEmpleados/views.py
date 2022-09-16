from django.shortcuts import render
from django.http import HttpResponse
from gestionEmpleados.models import Empleados
import datetime


def modificar_empleado(request): # aca mirar como hice en proyecta cac de flask para tener get y post juntas...
    if request.GET['emp']:
        pass
    elif request.POST['emp']:
        pass

def planilla_empleados(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    empleados=Empleados.objects.all()
    return render(request,"planilla_empleados.html", {"fecha":fecha_actual,"agno":anio,"empleados":empleados})

def busqueda_empleados(request):
    return render(request, "busqueda_empleados.html")

def buscar_empleado(request):
    if request.GET["emp"]:
        nombre_empleado= request.GET["emp"]
        empleados=Empleados.objects.filter(apellido_nombre__icontains=nombre_empleado)
        return render(request,"resultados_busqueda_empleado.html",{"empleados":empleados,"query":nombre_empleado})
    else:
        mensaje= "No has introducido ningún dato."
        return HttpResponse(mensaje)