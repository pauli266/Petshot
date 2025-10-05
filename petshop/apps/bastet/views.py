from django.shortcuts import render
from .models import Catalogo_Bastet, MetodoPago
from django.views import generic
from django.urls import reverse_lazy

# Catálogo Bastet
class Catalogo_BastetCrearVista(generic.CreateView):
    model = Catalogo_Bastet
    fields = '__all__'
    template_name = 'bastet/crear.html'
    success_url = reverse_lazy('bastet:listar-bastet') 

class Catalogo_BastetActualizarVista(generic.UpdateView):
    model = Catalogo_Bastet
    fields = '__all__'
    template_name = 'bastet/actualizar.html' 
    success_url = reverse_lazy('bastet:listar-bastet') 

class Catalogo_BastetEliminarVista(generic.DeleteView):
    model = Catalogo_Bastet
    template_name = 'bastet/eliminar.html'
    success_url = reverse_lazy('bastet:listar-bastet')  

class Catalogo_BastetLeerVista(generic.ListView):
    model = Catalogo_Bastet
    template_name = 'bastet/leer.html'
    context_object_name = 'bastets'  

# Métodos de Pago
class MetodoPagoLeerVista(generic.ListView):
    model = MetodoPago
    template_name = 'metodopago/leer.html'
    context_object_name = 'metodos_pago'

class MetodoPagoCrearVista(generic.CreateView):
    model = MetodoPago
    fields = ['nombre']
    template_name = 'metodopago/crear.html'
    success_url = reverse_lazy('bastet:listar-metodos')

class MetodoPagoActualizarVista(generic.UpdateView):
    model = MetodoPago
    fields = ['nombre']
    template_name = 'metodopago/actualizar.html'
    success_url = reverse_lazy('bastet:listar-metodos')

class MetodoPagoEliminarVista(generic.DeleteView):
    model = MetodoPago
    template_name = 'metodopago/eliminar.html'
    success_url = reverse_lazy('bastet:listar-metodos')
