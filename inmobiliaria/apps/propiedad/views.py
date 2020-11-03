from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

from .forms import PropiedadForm

def propiedadDetail(request, propiedad_id):

    propiedad = Propiedad.objects.get(id=propiedad_id)
    agente = Agente.objects.get(user=propiedad.agente)
    context = {
        'propiedad': propiedad,
        'agente': agente
    }
    return render(request, 'propiedad/propiedad-detail.html', context)

def propiedadList(request):

    propiedades = Propiedad.objects.all()
    context = {
        'propiedades': propiedades
    }

    return render(request, 'propiedad/propiedad-list.html', context)

def propiedadCreate(request):
    form = PropiedadForm(request.POST or None, request.FILES)

    context = {
        'form': form
    }
    if form.is_valid():
        propiedad = form.save(commit=False)

        propiedad.agente = request.user 
        propiedad.save()

        messages.success(request, 'Propiedad registrada con exito.')

        return HttpResponseRedirect("/")

    return render(request, 'propiedad/propiedad-form.html', context)  
