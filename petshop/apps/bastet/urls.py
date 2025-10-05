from django.urls import path, include
from apps.bastet.views import Catalogo_BastetActualizarVista, Catalogo_BastetCrearVista, Catalogo_BastetEliminarVista, Catalogo_BastetLeerVista
from apps.bastet.views import MetodoPagoLeerVista, MetodoPagoActualizarVista, MetodoPagoCrearVista, MetodoPagoEliminarVista
from django.contrib import admin

app_name = 'bastet'
urlpatterns = [
    path('admin/', admin.site.urls),  # ← ¡esto habilita el panel admin!
    path('bastet/', include('apps.bastet.urls')),  # tu app, por ejemplo
    # URLs para Catalogo_Bastet
    path('bastet/crear/', Catalogo_BastetCrearVista.as_view(), name='crear-bastet'),
    path('bastet/leer/', Catalogo_BastetLeerVista.as_view(), name='list-bastet'),
    path('bastet/actualizar/<int:pk>/', Catalogo_BastetActualizarVista.as_view(), name='actualizar-bastet'),
    path('bastet/eliminar/<int:pk>/', Catalogo_BastetEliminarVista.as_view(), name='eliminar-bastet'),

    # URLs para MetodoPago
    path('metodopago/leer/', MetodoPagoLeerVista.as_view(), name='listar-metodos'),
    path('metodopago/crear/', MetodoPagoCrearVista.as_view(), name='crear-metodo'),
    path('metodopago/actualizar/<int:pk>/', MetodoPagoActualizarVista.as_view(), name='actualizar-metodo'),
    path('metodopago/eliminar/<int:pk>/', MetodoPagoEliminarVista.as_view(), name='eliminar-metodo'),
]
