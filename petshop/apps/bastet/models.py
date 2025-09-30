from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class Catalogo(models.Model):
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    metodos_pago = models.ManyToManyField(MetodoPago)
    stock = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.producto}'