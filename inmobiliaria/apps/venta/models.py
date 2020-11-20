from django.db import models
from django.contrib.auth import get_user_model

from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

from .managers import VentaManager

User = get_user_model()

class Venta(models.Model):
    agente = models.ForeignKey(Agente, blank=True, related_name='%(class)s_agente', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, blank=True, related_name='%(class)s_usuario', on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, blank=True, on_delete=models.CASCADE)
    reserved = models.DateTimeField(verbose_name='Reservada', auto_now_add=True)
    completed = models.BooleanField(verbose_name='Completada', default=False)
    completed_date = models.DateTimeField(verbose_name='Completada', blank=True, null=True)

    objects = VentaManager()
