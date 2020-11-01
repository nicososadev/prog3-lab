from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Agente(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.user.name
