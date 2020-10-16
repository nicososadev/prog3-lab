from django.shortcuts import render

from apps.propiedad.models import Propiedad

def propiedadDetail(request, propiedad_id):

    propiedad = Propiedad.objects.get(id=propiedad_id)
    context = {
        'propiedad': propiedad
    }
    return render(request, 'propiedad-detail.html', context)

def propiedadList(request):

    propiedades = Propiedad.objects.all()
    context = {
        'propiedades': propiedades
    }

    return render(request, 'propiedad-list.html', context)

def propiedadCreate(request):

    return render(request, 'propiedad-form.html', {})  
