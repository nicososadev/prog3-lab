from django.db import models

class Mensaje(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    content = models.TextField(verbose_name='Mensaje', max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.email)
