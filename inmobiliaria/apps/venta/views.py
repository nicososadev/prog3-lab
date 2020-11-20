from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .models import Venta
from apps.propiedad.models import Propiedad
from apps.agente.models import Agente
from apps.user.decorators import allowed_users

User = get_user_model()

@login_required(login_url='/users/login/')
def ComprasList(request):

    user = request.user

    try:
        compras = Venta.objects.filter(usuario=user)
    except ObjectDoesNotExist:
        messages.error(request, 'Ocurrio un problema listando las compras')
        return redirect('core:home')

    context = {
        'compras': compras
    }

    return render(request, 'venta/compra-list.html', context)

@login_required(login_url='user:login')
@allowed_users(allowed_roles=['agente'])
def VentasList(request):

    user = request.user

    try:
        agente = Agente.objects.get(user=user)
        ventas = Venta.objects.filter(agente=agente)
        ventas_reservadas = ventas.filter(completed=False)
    except ObjectDoesNotExist:
        messages.error(request, 'Hubo un problema listando las ventas')
        return redirect('core:home')

    context = {
        'ventas': ventas_reservadas
    }

    return render(request, 'venta/venta-list.html', context)

@login_required(login_url='user:login')
@allowed_users(allowed_roles=['agente'])
def VentasCompletedList(request):

    user = request.user

    try:
        agente = Agente.objects.get(user=user)
        ventas = Venta.objects.filter(agente=agente)
        ventas_completadas = ventas.filter(completed=True)
    except ObjectDoesNotExist:
        messages.error(request, 'Hubo un problema listando las ventas completadas')
        return redirect('core:home')
    
    context = {
        'ventas': ventas_completadas
    }

    return render(request, 'venta/ventas-completed-list.html', context)

@login_required(login_url='user:login')
def VentaDetail(request, propiedad_id):

    try:
        propiedad = Propiedad.objects.get(id=propiedad_id)
        agente = Agente.objects.get(user__name=propiedad.agente.name)
    except ObjectDoesNotExist:
        messages.error(request, 'Hubo un problema procesando su compra')
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
        messages.error(request, 'Hubo un problema procesando su solicitud')
        return redirect('core:home')

    new_venta = Venta.objects.new_venta(agente, user, propiedad)

    propiedad.reserved = True
    propiedad.save()

    messages.success(request, 'Operacion realizada con éxito. Nuestro agente se pondrá en contacto contigo. Muchas gracias!')

    return redirect('core:home')

@login_required(login_url='/users/login/')
@allowed_users(allowed_roles=['agente'])
def VentaCompleted(request, venta_id):
    
    try:
        venta = Venta.objects.get(id=venta_id)
        propiedad = Propiedad.objects.get(id=venta.propiedad.id)
    except ObjectDoesNotExist:
        messages.error(request, 'Ha ocurrido un problema marcando la venta como completada')
        return redirect('venta:ventas')

    user = request.user

    if user != propiedad.agente:
        messages.error(request, 'No tienes permiso para modificar esta propiedad')
        return redirect('agente:propiedades')

    propiedad.reserved = False
    propiedad.sold_out = True
    propiedad.save()

    venta.completed = True
    venta.completed_date = timezone.now()
    venta.save()
    
    messages.success(request, 'Venta marcada como completada')

    return redirect ('/')

@login_required(login_url='/users/login/')
def VentaCancel(request, pk):
    
    try:
        venta = Venta.objects.get(id=pk)
        propiedad = Propiedad.objects.get(id=venta.propiedad.id)
    except expression as identifier:
        messages.error(request, 'Ha ocurrido un problema cancelando la venta')
        return redirect('core:home')

    propiedad.reserved = False
    propiedad.save()

    venta.delete()
    
    messages.success(request, 'Compra cancelada con éxito')

    return redirect ('/')
