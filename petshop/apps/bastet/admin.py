from django.contrib import admin
from .models import MetodoPago, Catalogo

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'precio', 'stock', 'contacto']
    search_fields = ['producto', 'contacto']
    list_filter = ['metodos_pago']
    filter_horizontal = ['metodos_pago']  # Para mejor interfaz al seleccionar muchos

    # Opcional: mostrar los métodos de pago en el listado como texto
    def mostrar_metodos_pago(self, obj):
        return ", ".join([m.nombre for m in obj.metodos_pago.all()])
    mostrar_metodos_pago.short_description = 'Métodos de Pago'
