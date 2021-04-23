from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

OPERATION = [
    ('AL', 'Alquiler'),
    ('VE', 'Venta'),
]

PROPERTY_TYPE = [
    ('CA', 'Casa'),
    ('DP', 'Departamento'),
]

class Propiedad(models.Model):

    agente = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    propType = models.CharField(max_length=2, choices=PROPERTY_TYPE, verbose_name = 'Tipo Propiedad')
    operation = models.CharField(max_length=2, choices=OPERATION, verbose_name = 'Tipo Operacion')
    description = models.TextField(max_length=200, verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Imagen', upload_to='propiedad/', null=True, blank=True)
    rooms = models.IntegerField(verbose_name = 'Habitaciones')
    bathrooms = models.IntegerField(verbose_name = 'Baños')
    surfice = models.IntegerField(verbose_name = 'Superficie')
    reserved = models.BooleanField(verbose_name='Reservada', default=False)
    sold_out = models.BooleanField(verbose_name='Vendida', default=False)
    featured = models.BooleanField(verbose_name='Promocionada', default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Actualizado')
    #comentario
    class Meta:
        verbose_name = 'propiedad'
        verbose_name_plural = 'propiedades'
        ordering = ['-created']

    def precio(self):
        return '$ %.2f' % self.price

    def get_absolute_url(self):
        return reverse('propiedad:detail', kwargs={'propiedad_id': self.id})

    def __str__(self):
        return  '%s' % self.id