from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Venta
from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

User = get_user_model()

@login_required(login_url='/users/login/')
def ComprasList(request):

    user = request.user

    compras = Venta.objects.filter(usuario=user)

    context = {
        'compras': compras
    }

    return render(request, 'venta/compra-list.html', context)

def VentasList(request):

    user = request.user
    agente = Agente.objects.get(user=user)
    ventas = Venta.objects.filter(agente=agente)

    context = {
        'ventas': ventas
    }

    return render(request, 'venta/venta-list.html', context)

@login_required(login_url='user:login')
def VentaDetail(request, propiedad_id):
    propiedad = Propiedad.objects.get(id=propiedad_id)
    agente = Agente.objects.get(user__name=propiedad.agente.name)

    context = {
        'propiedad': propiedad,
        'agente': agente
    }

    return render(request, 'venta/venta-confirm.html', context)

@login_required(login_url='user:login')
def VentaConfirm(request, propiedad_id):

    propiedad = Propiedad.objects.get(id=propiedad_id)
    agente = Agente.objects.get(user__name=propiedad.agente.name)
    user = request.user

    new_venta = Venta.objects.new_venta(agente, user, propiedad)

    propiedad.sold_out = True

    propiedad.save()

    messages.success(request, 'Operacion realizada con éxito. Nuestro agente se pondrá en contacto contigo. Muchas gracias!')

    return redirect('core:home')

@login_required(login_url='/users/login/')
def VentaCancel(request, pk):
    
    venta = Venta.objects.get(id=pk)
    propiedad = Propiedad.objects.get(id=venta.propiedad.id)

    propiedad.sold_out = False

    propiedad.save()

    venta.delete()
    
    messages.success(request, 'Compra cancelada con éxito')

    return redirect ('/')
