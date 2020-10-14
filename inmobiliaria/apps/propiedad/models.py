from django.db import models

COLORS = [
    ('WH', 'Blanco'),
    ('GR', 'Verde'),
    ('YE', 'Amarillo'),
]

class Propiedad(models.Model):

    description = models.TextField()
    colors = models.CharField(max_length=2, choices=COLORS)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    