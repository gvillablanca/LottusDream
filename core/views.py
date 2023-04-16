from django.shortcuts import render

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

