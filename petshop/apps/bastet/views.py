from django.shortcuts import render
from .models import Bastet
from django.views import generic
from django.urls import reverse_lazy

# Bastet
class BastetCrearVista(generic.CreateView):
    model = Bastet
    fields = '__all__'
    template_name = 'bastet/crear.html'
    success_url = reverse_lazy('bastet:list-bastet') 
    
class BastetActualizarVista(generic.UpdateView):
    model = Bastet
    fields = '__all__'
    template_name = 'bastet/actualizar.html' 
    success_url = reverse_lazy('bastet:list-bastet') 

class BastetEliminarVista(generic.DeleteView):
    model = Bastet
    template_name = 'bastet/eliminar.html'
    success_url = reverse_lazy('bastet:list-beste')  

class BastetLeerVista(generic.ListView):
    model = Bastet
    template_name = 'bastet/leer.html'
    context_object_name = 'bastet'  
