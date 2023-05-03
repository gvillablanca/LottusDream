from django.urls import path, include
from .views import home, administrador, registroUsuario, solicitud, usuario, registro ,pruebasRender, CotizacionViewset, SalonViewset, ProveedorViewset, ServicioViewset, UsuarioViewset, EventoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cotizacion', CotizacionViewset)
router.register('salon', SalonViewset)
router.register('proveedor', ProveedorViewset)
router.register('servicio', ServicioViewset)
router.register('usuario', UsuarioViewset)
router.register('cotizacion', EventoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('administrador/', administrador, name="administrador"),
    path('registroUsuario/', registroUsuario, name="registroUsuario"),
    path('registro/', registro, name="registro"),
    path('solicitud/', solicitud, name="solicitud"),
    path('usuario/', usuario, name="usuario"),
    path('pruebasRender/', pruebasRender, name="pruebasRender"), 
    path('api/', include(router.urls)),
]