from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import Template, Context
from .models import Usuario, Cotizacion, Evento, Proveedor, Salon, Servicio
from .forms import CotizacionForm, UsuarioForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from .serializer import CotizacionSerializer,EventoSerializer, ProveedorSerializer, ServicioSerializer, UsuarioSerializer, SalonSerializer

class CotizacionViewset(viewsets.ModelViewSet):
    queryset =Cotizacion.objects.all()  
    serializer_class = CotizacionSerializer

class EventoViewset(viewsets.ModelViewSet):
    queryset =Evento.objects.all()  
    serializer_class = EventoSerializer

class ProveedorViewset(viewsets.ModelViewSet):
    queryset =Proveedor.objects.all()  
    serializer_class = ProveedorSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset =Usuario.objects.all()  
    serializer_class = UsuarioSerializer

class SalonViewset(viewsets.ModelViewSet):
    queryset =Salon.objects.all()  
    serializer_class = SalonSerializer

class ServicioViewset(viewsets.ModelViewSet):
    queryset =Servicio.objects.all()  
    serializer_class = ServicioSerializer

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

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
    data = {
        'form': CotizacionForm()
    }

    if request.method == 'POST':
        formulario = CotizacionForm(data=request.POST)
        if  formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Solicitud enviada, te contactaremos pronto"
            print(formulario)
            print("a")
        else:
            data["form"] = formulario
            print(formulario)
            print("b")

    return render(request, 'core/solicitud.html', data)

def registroUsuario(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if  formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Solicitud enviada, te contactaremos pronto"
            print(formulario)
            print("a")
        else:
            data["form"] = formulario
            print(formulario)
            print("b")

    return render(request, 'core/RegistrarUsuario.html', data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if  formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "usuario registrado correctamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'registration/registro.html', data)


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

