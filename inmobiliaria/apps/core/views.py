from django.shortcuts import render

from apps.propiedad.models import Propiedad

def HomePage(request):

    propiedades = Propiedad.objects.all()
    context = {
        'propiedades': propiedades
    }
    return render(request, 'core/homepage.html', context)