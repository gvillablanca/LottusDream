from django.urls import path
from .views import home, administrador, home2, registroUsuario, solicitud, usuario, empv

urlpatterns = [
    path('', home, name="home"),
    path('home2/', home2, name="home2"),
    path('administrador/', administrador, name="administrador"),
    path('registroUsuario/', registroUsuario, name="registroUsuario"),
    path('solicitud/', solicitud, name="solicitud"),
    path('usuario/', usuario, name="usuario"),
    path('emp/', empv, name="empv"),    
]