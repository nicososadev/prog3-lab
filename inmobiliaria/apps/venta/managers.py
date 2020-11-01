from django.db import models

class VentaManager(models.Manager):

    def new_venta(self, agente, usuario, propiedad):

        venta = self.create(agente=agente, usuario=usuario, propiedad=propiedad)

        return venta