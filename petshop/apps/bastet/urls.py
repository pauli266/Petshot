from django.urls import path
from apps.bastet.views import BastetActualizarVista, BastetCrearVista, BastetEliminarVista, BastetLeerVista
from django.contrib import admin

app_name = 'bastet'
urlpatterns = [
    path ('crear/', BastetCrearVista.as_view(), name = 'crear-bastet'),
    path ('leer/', BastetLeerVista.as_view(), name = 'list-bastet'),
    path ('actualizar/<int:pk>/', BastetActualizarVista.as_view(), name = 'actualizar-bastet'),
    path ('eliminar/<int:pk>/', BastetEliminarVista.as_view(), name = 'eliminar-bastet'),
]