from django.contrib import admin
from .models import MetodoPago, Catalogo_Bastet

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Catalogo_Bastet)
class CatalogoBastetAdmin(admin.ModelAdmin):
    list_display = ['producto', 'precio', 'stock', 'contacto', 'mostrar_metodos_pago']
    search_fields = ['producto', 'contacto']
    list_filter = ['metodos_pago']
    filter_horizontal = ['metodos_pago']  # Mejor interfaz para ManyToMany

    def mostrar_metodos_pago(self, obj):
        return ", ".join([metodo.nombre for metodo in obj.metodos_pago.all()])
    mostrar_metodos_pago.short_description = 'Métodos de Pago'
