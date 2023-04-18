from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Administrador

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def home2(request):
    return render(request, 'core/index2.html')

def usuario(request):
    return render(request, 'core/perfil-usuario.html')

def administrador(request):
    return render(request, 'core/administrador.html')

def solicitud(request):
    return render(request, 'core/solicitud.html')

def registroUsuario(request):
    return render(request, 'core/RegistrarUsuario.html')

def pruebas(request):
    return render(request, 'core/prueba.html')

#pruebas conexion base de datos
def pruebasRender(request):
    objects = Administrador.objects.all()
    count = 0

    for emp in objects:
        if count == 4:
            res = '&nbsp;&nbsp;&nbsp;&nbsp;' + emp.rut_admin + \
                ' ' + emp.nombre + '&nbsp;&nbsp;&nbsp;&nbsp;||</p>'
            count = 0 
        else:
            if count == 0:
                res = ''+'||'
            res += '' + emp.rut_admin + \
                ' ' + emp.nombre + '||'
            count += 1

    nombre = "emilia"
    plantillaExterna = open("../LottusDream/core/templates/core/prueba.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto=Context({"nombre": res})
    documento=template.render(contexto)
    return HttpResponse(documento)