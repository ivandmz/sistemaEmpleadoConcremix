from django.shortcuts import render,redirect
from django.http import HttpResponse
from gestionEmpleados.models import Empleado, Vehiculo, Sector
from gestionEmpleados.forms import FormuCrearEmpleado, FormuEditarEmpleado, FormuCrearVehiculo, FormuCrearSector
from django.contrib import messages
import datetime, os
from sistemaEmpleadosConcremix import settings


# EMPLEADOS
def crear_empleado(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.method == 'POST':
        form_empleado = FormuCrearEmpleado(request.POST,request.FILES)
        if form_empleado.is_valid():
            Empleado.objects.create(**form_empleado.cleaned_data)
            messages.success(request,"Empleado cargado satisfactoriamente.")
        else:
            messages.error(request,"Datos del formulario inválidos")
        return redirect('Empleados')
    else:
        return render(request, "gestionEmpleados/crear_empleado.html", {"fecha":fecha_actual,"agno":anio}) # GET. me sirve el form para crear/ingresar empleado

def editar_empleado(request,id):
    """ Función que edita un empleado buscandolo en BD con su número id"""
    empleado = Empleado.objects.get(pk=id)
    form_empleado = FormuEditarEmpleado(instance=empleado)
    if request.method == 'POST':
        if request.FILES and empleado.foto:
            os.remove(os.path.join(settings.MEDIA_ROOT + '/' + str(empleado.foto)))
        form_empleado = FormuEditarEmpleado(request.POST,request.FILES, instance=empleado)
        if form_empleado.is_valid():
            form_empleado.save()
            # empleado.update(**form_empleado.cleaned_data)
            messages.success(request,"Empleado actualizado satisfactoriamente")
        else:
            print(form_empleado.errors) # esto en produccion se va...
            messages.error(request,"Datos incorrectos en formulario")
        return redirect('Empleados')
    else:
        fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
        anio=datetime.datetime.now().strftime("%Y")
        return render(request, "gestionEmpleados/editar_empleado.html", {"form_empleado":form_empleado,"fecha":fecha_actual,"agno":anio})

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
    messages.info(request,"Estado modificado con éxito")
    return redirect('Empleados')

def planilla_empleados(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    empleados=Empleado.objects.all().order_by('apellido_nombre')
    return render(request,"gestionEmpleados/planilla_empleados.html", {"fecha":fecha_actual,"agno":anio,"empleados":empleados})

def busqueda_empleados(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.method == 'POST':
        if request.POST["emp"]:
            nombre_empleado= request.POST["emp"]
            empleados=Empleado.objects.filter(apellido_nombre__icontains=nombre_empleado).order_by('apellido_nombre')
            messages.info(request,"Búsqueda realizada")
            return render(request,"gestionEmpleados/resultados_busqueda_empleado.html",{"empleados":empleados,"query":nombre_empleado,"fecha":fecha_actual,"agno":anio})
        else:
            messages.warning(request,"No has introducido ningún dato")
            return redirect('Empleados')
    return render(request, "gestionEmpleados/busqueda_empleados.html", {"fecha":fecha_actual,"agno":anio})


# VEHICULOS
def planilla_vehiculos(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    vehiculos = Vehiculo.objects.all().order_by('interno')
    return render(request,"gestionEmpleados/planilla_vehiculos.html", {"fecha":fecha_actual,"agno":anio,"vehiculos":vehiculos})

def busqueda_vehiculos(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.method == 'POST':
        if request.POST["vehi"]:
            nombre_vehiculo= request.POST["vehi"]
            vehiculos=Vehiculo.objects.filter(nombre_vehiculo__icontains=nombre_vehiculo).order_by('interno')
            messages.info(request,"Búsqueda realizada")
            return render(request,"gestionEmpleados/resultados_busqueda_vehiculo.html",{"vehiculos":vehiculos,"query":nombre_vehiculo,"fecha":fecha_actual,"agno":anio})
        else:
            messages.warning(request,"No has introducido ningún dato")
            return redirect('Vehiculos')
            
    else:
        return render(request, "gestionEmpleados/busqueda_vehiculos.html", {"fecha":fecha_actual,"agno":anio})

def crear_vehiculo(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    form_vehiculo = FormuCrearVehiculo()
    if request.method == 'POST':
        form_vehiculo = FormuCrearVehiculo(request.POST) # como hago para no repetir esto?
        if form_vehiculo.is_valid():
            Vehiculo.objects.create(**form_vehiculo.cleaned_data) # hace falta la variable realmente???
            messages.success(request,"Vehículo cargado correctamente")
        else:
            messages.error(request,"Datos de formulario incorrectos")
        return redirect('Vehiculos')
    else:
        return render(request, "gestionEmpleados/crear_vehiculo.html", {"fecha":fecha_actual,"agno":anio,"form_vehiculo":form_vehiculo}) # me sirve el form para crear/ingresar un vehiculo
        
def editar_vehiculo(request,id):
    """ Función que edita un vehículo buscandolo de la BD con su número id"""
    vehiculo = Vehiculo.objects.filter(id=id)
    form_vehiculo = FormuCrearVehiculo(instance=vehiculo.first())
    if request.method == 'POST':
        form_vehiculo = FormuCrearVehiculo(request.POST)
        print(form_vehiculo)
        if form_vehiculo.is_valid():
            vehiculo.update(**form_vehiculo.cleaned_data)
            messages.success(request,"Vehículo actualizado correctamente")
        else:
            print(form_vehiculo.errors) # en produccion esto se va
            messages.error(request,"Algún dato del formulario es incorrecto")
        return redirect('Vehiculos')
    else:
        fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
        anio=datetime.datetime.now().strftime("%Y")
        return render(request, "gestionEmpleados/editar_vehiculo.html", {"form_vehiculo":form_vehiculo,"fecha":fecha_actual,"agno":anio})

def eliminar_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    messages.warning(request,"Vehículo eliminado")
    return redirect('Vehiculos')

# SECTORES
def planilla_sectores(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    sectores = Sector.objects.all().order_by('nombre_sector')
    return render(request,"gestionEmpleados/planilla_sectores.html", {"fecha":fecha_actual,"agno":anio,"sectores":sectores})

def busqueda_sectores(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    if request.method == 'POST':
        if request.POST["sector"]:
            nombre_sector= request.POST["sector"]
            sectores=Sector.objects.filter(nombre_sector__icontains=nombre_sector).order_by('nombre_sector')
            messages.info(request,"Búsqueda realizada")
            return render(request,"gestionEmpleados/resultados_busqueda_sector.html",{"sectores":sectores,"query":nombre_sector,"fecha":fecha_actual,"agno":anio})
        else:
            messages.warning(request,"No has introducido ningún dato")
            return redirect('Sectores')
            
    else:
        return render(request, "gestionEmpleados/busqueda_sectores.html", {"fecha":fecha_actual,"agno":anio})

def crear_sector(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    form_sector = FormuCrearSector()
    if request.method == 'POST':
        form_sector = FormuCrearSector(request.POST) # como hago para no repetir esto?
        if form_sector.is_valid():
            Sector.objects.create(**form_sector.cleaned_data) # hace falta la variable realmente???
            messages.success(request,"Sector creado satisfactoriamente")
        else:
            messages.error(request,"Datos de formulario incorrectos")
        return redirect('Sectores')
    else:
        return render(request, "gestionEmpleados/crear_sector.html", {"fecha":fecha_actual,"agno":anio,"form_sector":form_sector}) # me sirve el form para crear/ingresar sector
        
def editar_sector(request,id):
    """ Función que edita un sector buscandolo de la BD con su número id"""
    sector = Sector.objects.filter(id=id)
    form_sector = FormuCrearSector(instance=sector.first())
    if request.method == 'POST':
        form_sector = FormuCrearSector(request.POST)
        print(form_sector) # en produccion se va...
        if form_sector.is_valid():
            sector.update(**form_sector.cleaned_data)
            messages.success(request,"Sector actualizado correctamente")
        else:
            print(form_sector.errors) # en produccion esto se va
            messages.error(request,"Algún dato del formulario es incorrecto")
        return redirect('Sectores')
    else:
        fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
        anio=datetime.datetime.now().strftime("%Y")
        return render(request, "gestionEmpleados/editar_sector.html", {"form_sector":form_sector,"fecha":fecha_actual,"agno":anio})

def eliminar_sector(request,id):
    sector = Sector.objects.get(id=id)
    sector.delete()
    messages.warning(request,"Sector eliminado")
    return redirect('Sectores')