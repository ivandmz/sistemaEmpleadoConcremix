from django.shortcuts import render,redirect
from django.http import HttpResponse
from gestionEmpleados.models import Empleado, Vehiculo, Recinto
from gestionEmpleados.forms import FormuCrearEmpleado, FormuCrearVehiculo
import datetime


# EMPLEADOS
def crear_empleado(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.method == 'POST':
        form_empleado = FormuCrearEmpleado(request.POST,request.FILES)
        if form_empleado.is_valid():
            empleado = Empleado.objects.create(**form_empleado.cleaned_data)
        else:
            raise ValueError("formulario no valido")
        return redirect('Empleados')
    else:
        return render(request, "gestionEmpleados/crear_empleado.html", {"fecha":fecha_actual,"agno":anio}) # GET. me sirve el form para crear/ingresar empleado
        
def editar_empleado(request,id):
    id_empleado= id
    empleado = Empleado.objects.filter(id=id_empleado)
    if request.method == 'POST':
        form_empleado = FormuCrearEmpleado(request.POST,request.FILES)
        if form_empleado.is_valid():
            empleado.update(**form_empleado.cleaned_data)
        else:
            print(form_empleado.errors)
            raise ValueError("formulario no valido")
        return redirect('Empleados')
    else:
        fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
        anio=datetime.datetime.now().strftime("%Y")
        return render(request, "gestionEmpleados/editar_empleado.html", {"empleado":empleado,"fecha":fecha_actual,"agno":anio})

def alta_baja(request,id):
    id_empleado = id
    empleado = Empleado.objects.get(id=id_empleado)
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
    empleados=Empleado.objects.all().order_by('apellido_nombre')
    return render(request,"gestionEmpleados/planilla_empleados.html", {"fecha":fecha_actual,"agno":anio,"empleados":empleados})

def busqueda_empleados(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    return render(request, "gestionEmpleados/busqueda_empleados.html", {"fecha":fecha_actual,"agno":anio})

def buscar_empleado(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.GET["emp"]:
        nombre_empleado= request.GET["emp"]
        empleados=Empleado.objects.filter(apellido_nombre__icontains=nombre_empleado).order_by('apellido_nombre')
        return render(request,"gestionEmpleados/resultados_busqueda_empleado.html",{"empleados":empleados,"query":nombre_empleado,"fecha":fecha_actual,"agno":anio})
    else:
        mensaje= "No has introducido ningún dato."
        return HttpResponse(mensaje)

# VEHICULOS
def planilla_vehiculos(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    vehiculos = Vehiculo.objects.all().order_by('interno')
    return render(request,"gestionEmpleados/planilla_vehiculos.html", {"fecha":fecha_actual,"agno":anio,"vehiculos":vehiculos})

def busqueda_vehiculos(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.method == 'GET':
        if request.GET["vehi"]:
            nombre_vehiculo= request.GET["vehi"]
            vehiculos=Vehiculo.objects.filter(nombre_vehiculo__icontains=nombre_vehiculo).order_by('interno')
            return render(request,"gestionEmpleados/resultados_busqueda_vehiculo.html",{"vehiculos":vehiculos,"query":nombre_vehiculo,"fecha":fecha_actual,"agno":anio})
        else:
            mensaje= "No has introducido ningún dato."
            return HttpResponse(mensaje)
    else:
        return render(request, "gestionEmpleados/busqueda_vehiculos.html", {"fecha":fecha_actual,"agno":anio})

def crear_vehiculo(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    form_vehiculo = FormuCrearVehiculo()
    if request.method == 'POST':
        form_vehiculo = FormuCrearVehiculo(request.POST) # como hago para no repetir esto?
        if form_vehiculo.is_valid():
            vehiculo = Vehiculo.objects.create(**form_vehiculo.cleaned_data) # hace falta la variable realmente???
        else:
            raise ValueError("formulario no valido")
        return redirect('Vehiculos')
    else:
        return render(request, "gestionEmpleados/crear_vehiculo.html", {"fecha":fecha_actual,"agno":anio,"form_vehiculo":form_vehiculo}) # me sirve el form para crear/ingresar empleado
        

# RECINTOS