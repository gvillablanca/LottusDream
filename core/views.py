from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Usuario, Cotizacion, Evento, Proveedor, Salon, Servicio_evento

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def home2(request):
    return render(request, 'core/index2.html')

def usuario(request):
    return render(request, 'core/perfil-usuario.html')

def administrador(request):
    objectsU = Usuario.objects.all()
    objectsCot = Cotizacion.objects.all()
    objectsEvt = Evento.objects.all()
    objectsProv = Proveedor.objects.all()
    objectsSal = Salon.objects.all()
    nombre_administrador = ''
    correo = ''
    cargo = ''
    ubicacion = ''

    for admin in objectsU:
        if admin.tipo == "ADMINISTRADOR":
            nombre_administrador = admin.nombre + ' ' + admin.apellido
            correo = admin.correo
            cargo = admin.cargo
            ubicacion = admin.oficina    

    plantillaExterna = open("../LottusDream/core/templates/core/administrador.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto=Context({"cotizaciones":objectsCot, "evento": objectsEvt, "salon": objectsSal, "proveedor": objectsProv, "usuarios": objectsU, "nombre_administrador":nombre_administrador, "correo":correo, "cargo":cargo, "ubicacion":ubicacion})
    documento=template.render(contexto)
    return HttpResponse(documento)

def solicitud(request):
    return render(request, 'core/solicitud.html')

def registroUsuario(request):
    return render(request, 'core/RegistrarUsuario.html')

#pruebas conexion base de datos
def pruebasRender(request):
    objectsU = Usuario.objects.all()
    objectsCot = Cotizacion.objects.all()

    plantillaExterna = open("../LottusDream/core/templates/core/prueba.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto=Context({"usuarios": objectsU, "cotizaciones":objectsCot})
    documento=template.render(contexto)
    return HttpResponse(documento)


