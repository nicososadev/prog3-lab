from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import Venta
from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

User = get_user_model()

@login_required(login_url='/users/login/')
def ComprasList(request):

    user = request.user

    try:
        compras = Venta.objects.filter(usuario=user)
    except ObjectDoesNotExist:
        messages.error('Ocurrio un problema listando las compras')
        return redirect('core:home')

    context = {
        'compras': compras
    }

    return render(request, 'venta/compra-list.html', context)

@login_required(login_url='user:login')
def VentasList(request):

    user = request.user

    try:
        agente = Agente.objects.get(user=user)
        ventas = Venta.objects.filter(agente=agente)
    except ObjectDoesNotExist:
        messages.error('Hubo un problema listando las ventas')
        return redirect('core:home')

    context = {
        'ventas': ventas
    }

    return render(request, 'venta/venta-list.html', context)

@login_required(login_url='user:login')
def VentaDetail(request, propiedad_id):

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
        agente = Agente.objects.get(user__name=propiedad.agente.name)
    except ObjectDoesNotExist:
        messages.error('Hubo un problema procesando su compra')
        return redirect('core:home')

    context = {
        'propiedad': propiedad,
        'agente': agente
    }

    return render(request, 'venta/venta-confirm.html', context)

@login_required(login_url='user:login')
def VentaConfirm(request, propiedad_id):

    user = request.user

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
        agente = Agente.objects.get(user__name=propiedad.agente.name)
    except ObjectDoesNotExist:
        messages.error('Hubo un problema procesando su compra')
        return redirect('core:home')

    new_venta = Venta.objects.new_venta(agente, user, propiedad)

    propiedad.sold_out = True
    propiedad.save()

    messages.success(request, 'Operacion realizada con éxito. Nuestro agente se pondrá en contacto contigo. Muchas gracias!')

    return redirect('core:home')

@login_required(login_url='/users/login/')
def VentaCancel(request, pk):
    
    try:
        venta = Venta.objects.get(id=pk)
        propiedad = Propiedad.objects.get(id=venta.propiedad.id)
    except expression as identifier:
        messages.error('Ha ocurrido un problema cancelando la venta')
        return redirect('core:home')

    propiedad.sold_out = False
    propiedad.save()

    venta.delete()
    
    messages.success(request, 'Compra cancelada con éxito')

    return redirect ('/')
