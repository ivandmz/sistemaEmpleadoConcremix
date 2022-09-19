from django.shortcuts import render
from django.http import HttpResponse
from gestionEmpleados.models import Empleados
from gestionEmpleados.forms import FormuCrearEmpleado
import datetime


def crear_empleado(request): # aca mirar como hice en proyecta cac de flask para tener get y post juntas...
    if request.method == 'POST':
        form_crear_empleado = FormuCrearEmpleado(request.POST)
        if form_crear_empleado.is_valid():
            form_crear_empleado = form_crear_empleado.cleaned_data # devuelve (o transforma?) en dict...
            # aca debo operar con variable y poner cada dato del post
    else:
        return render(request, "gestionEmpleados/crear_empleado.html") # GET. me sirve el form para crear/ingresar empleado
        
def modificar_empleado(request): # aca mirar como hice en proyecta cac de flask para tener get y post juntas...
    if request.GET['emp']:
        pass
    elif request.POST['emp']:
        pass

def planilla_empleados(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    empleados=Empleados.objects.all()
    return render(request,"gestionEmpleados/planilla_empleados.html", {"fecha":fecha_actual,"agno":anio,"empleados":empleados})

def busqueda_empleados(request):
    return render(request, "gestionEmpleados/busqueda_empleados.html")

def buscar_empleado(request):
    if request.GET["emp"]:
        nombre_empleado= request.GET["emp"]
        empleados=Empleados.objects.filter(apellido_nombre__icontains=nombre_empleado)
        return render(request,"gestionEmpleados/resultados_busqueda_empleado.html",{"empleados":empleados,"query":nombre_empleado})
    else:
        mensaje= "No has introducido ningún dato."
        return HttpResponse(mensaje)