from django.shortcuts import render,redirect
from django.http import HttpResponse
from gestionEmpleados.models import Empleados
from gestionEmpleados.forms import FormuCrearEmpleado
import datetime


def crear_empleado(request):
    if request.method == 'POST':
        form_empleado = FormuCrearEmpleado(request.POST,request.FILES)
        if form_empleado.is_valid():
            empleado = Empleados.objects.create(**form_empleado.cleaned_data)
        else:
            raise ValueError("formulario no valido")
        return redirect('Empleados')
    else:
        return render(request, "gestionEmpleados/crear_empleado.html") # GET. me sirve el form para crear/ingresar empleado
        
def editar_empleado(request,id):
    id_empleado= id
    empleado = Empleados.objects.filter(id=id_empleado)
    if request.method == 'POST':
        form_empleado = FormuCrearEmpleado(request.POST,request.FILES)
        if form_empleado.is_valid():
            empleado.update(**form_empleado.cleaned_data)
        else:
            print(form_empleado.errors)
            raise ValueError("formulario no valido")
        return redirect('Empleados')
    else:
        return render(request, "gestionEmpleados/editar_empleado.html", {"empleado":empleado})

def alta_baja(request,id):
    id_empleado = id
    empleado = Empleados.objects.get(id=id_empleado)
    if empleado.activo == True:
        empleado.fecha_baja = datetime.datetime.now()
        empleado.activo = False
    elif empleado.activo == False:
        empleado.fecha_baja = None
        empleado.fecha_ingreso = datetime.datetime.now()
        empleado.activo = True
    empleado.save()
    return redirect('Empleados')

def planilla_empleados(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    empleados=Empleados.objects.all().order_by('apellido_nombre')
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
