from django.shortcuts import render
from django.http import HttpResponse
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


#prueba de conexion a la base de datos
def empv(request):
    res = """<h2 align="center">administradores</h2>
             <hr>"""
    objects = Administrador.objects.all()
    count = 0

    for emp in objects:
        if count == 4:
            res += '&nbsp;&nbsp;&nbsp;&nbsp;' + emp.rut_admin + \
                ' ' + emp.nombre + '&nbsp;&nbsp;&nbsp;&nbsp;||</p>'
            count = 0 
        else:
            if count == 0:
                res += '<p align="center">'+'||'
            res += '&nbsp;&nbsp;&nbsp;&nbsp;' + emp.rut_admin + \
                ' ' + emp.nombre + '&nbsp;&nbsp;&nbsp;&nbsp;||'
            count += 1

    return HttpResponse(res)

