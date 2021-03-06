from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

from .forms import PropiedadForm
from apps.user.decorators import allowed_users

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
    precio_min = request.GET.get('precio-min')
    precio_max = request.GET.get('precio-max')

    if propType != '' and propType is not None:
        propiedades = propiedades.filter(propType=propType)

    if operation != '' and operation is not None:
        propiedades = propiedades.filter(operation=operation)

    if rooms != '' and rooms is not None:
        propiedades = propiedades.filter(rooms=rooms)

    if bathrooms != '' and bathrooms is not None:
        propiedades = propiedades.filter(bathrooms=bathrooms)

    if precio_min != '' and precio_min is not None:
        propiedades = propiedades.filter(price__gte=precio_min)

    if precio_max != '' and precio_max is not None:
        propiedades = propiedades.filter(price__lte=precio_max)
        
    context = {
        'propiedades': propiedades
    }

    return render(request, 'propiedad/propiedad-list.html', context)

@login_required(login_url='/users/login/')
@allowed_users(allowed_roles=['agente'])
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

@login_required(login_url='/users/login/')
@allowed_users(allowed_roles=['agente'])
def propiedadUpdate(request, propiedad_id):

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
    except ObjectDoesNotExist:
        messages.error(request, 'Propiedad no encontrada')
        return redirect('agente:propiedades')

    user = request.user

    if user != propiedad.agente:
        messages.error(request, 'No tienes permiso para modificar esta propiedad')
        return redirect('agente:propiedades')
    
    if propiedad.reserved:
        messages.error(request, 'No es posible actualizar una propiedad reservada')
        return redirect('agente:propiedades')

    if propiedad.sold_out:
        messages.error(request, 'No es posible actualizar una propiedad vendida')
        return redirect('agente:propiedades')

    form = PropiedadForm(request.POST or None, request.FILES or None, instance=propiedad)

    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            propiedad = form.save(commit=False)

            propiedad.agente = request.user 
            propiedad.save()

            messages.success(request, 'Propiedad actualizada con exito.')

            return redirect('agente:propiedades')

    return render(request, 'propiedad/propiedad-update-form.html', context)   


@login_required(login_url='/users/login/')
@allowed_users(allowed_roles=['agente'])
def propiedadDeleteConfirm(request, propiedad_id):

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
    except ObjectDoesNotExist:
        messages.error(request, 'Propiedad no encontrada')
        return redirect('agente:propiedades')

    user = request.user

    if user != propiedad.agente:
        messages.error(request, 'No tienes permiso para eliminar esta propiedad')
        return redirect('agente:propiedades')

    if propiedad.reserved:
        messages.error(request, 'No es posible eliminar una propiedad reservada')
        return redirect('agente:propiedades')

    if propiedad.sold_out:
        messages.error(request, 'No es posible eliminar una propiedad vendida')
        return redirect('agente:propiedades')

    context = {
        'propiedad': propiedad
    }

    return render(request, 'propiedad/propiedad-delete.html', context) 

@login_required(login_url='/users/login/')
@allowed_users(allowed_roles=['agente'])
def propiedadDelete(request, propiedad_id):

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
    except ObjectDoesNotExist:
        messages.error(request, 'Propiedad no encontrada')
        return redirect('agente:propiedades')

    user = request.user

    if user != propiedad.agente:
        messages.error(request, 'No tienes permiso para eliminar esta propiedad')
        return redirect('agente:propiedades')

    if propiedad.reserved:
        messages.error(request, 'No es posible eliminar una propiedad reservada')
        return redirect('agente:propiedades')

    if propiedad.sold_out:
        messages.error(request, 'No es posible eliminar una propiedad vendida')
        return redirect('agente:propiedades')

    propiedad.delete()

    messages.success(request, 'Propiedad eliminada con éxito')

    return redirect('agente:propiedades')