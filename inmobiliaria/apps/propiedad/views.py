from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

from .forms import PropiedadForm

def propiedadDetail(request, propiedad_id):

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
        agente = Agente.objects.get(user=propiedad.agente)
    except ObjectDoesNotExist:
        messages.error(request, 'Propiedad no encontrada')
        return redirect('core:home')

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

def propiedadListFilter(request):

    propiedades = Propiedad.objects.all()

    propType = request.GET.get('tipo')
    operation = request.GET.get('operacion')
    rooms = request.GET.get('rooms')
    bathrooms = request.GET.get('bathrooms')

    if propType != '' and propType is not None:
        porpiedades = propiedades.filter(propType=propType)

    if operation != '' and operation is not None:
        porpiedades = propiedades.filter(operation=operation)

    if rooms != '' and rooms is not None:
        porpiedades = propiedades.filter(rooms=rooms)

    if bathrooms != '' and bathrooms is not None:
        porpiedades = propiedades.filter(bathrooms=bathrooms)   
        
    context = {
        'propiedades': porpiedades
    }

    return render(request, 'propiedad/propiedad-list.html', context)

@login_required
def propiedadCreate(request):
    form = PropiedadForm(request.POST or None, request.FILES or None)

    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            propiedad = form.save(commit=False)

            propiedad.agente = request.user 
            propiedad.save()

            messages.success(request, 'Propiedad registrada con exito.')

            return HttpResponseRedirect("/")

    return render(request, 'propiedad/propiedad-form.html', context)  
