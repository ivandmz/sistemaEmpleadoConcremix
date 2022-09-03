from django.http import HttpResponse
from django.template import Template,Context, loader
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def index(request):
    fecha_actual=datetime.datetime.now().strftime("%D - %H:%M:%S")
    anio=datetime.datetime.now().strftime("%Y")
    return render(request,"index.html", {"fecha":fecha_actual,"agno":anio})