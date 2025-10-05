from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField("Nombre del método de pago", max_length=50)

    def __str__(self):
        return self.nombre


class Catalogo_Bastet(models.Model):
    producto = models.CharField("Nombre del producto", max_length=100)
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    metodos_pago = models.ManyToManyField(MetodoPago, verbose_name="Métodos de pago")
    stock = models.CharField("Estado del stock", max_length=100)
    contacto = models.CharField("Información de contacto", max_length=100)

    def __str__(self):
        return self.producto
