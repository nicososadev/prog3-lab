from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Venta
from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

User = get_user_model()

def VentasList(request):

    user = request.user

    ventas = Venta.objects.filter(usuario=user)

    context = {

        'ventas': ventas
    }

    return render(request, 'venta/venta-list.html', context)

def VentaDetail(request):
    pass

def VentaConfirm(request):
    agente_id = request.POST.get('agente')
    ususario_id = request.POST.get('usuario')
    propiedad_id = request.POST.get('propiedad')
    
    agente = Agente.objects.get(id=agente_id)
    ususario = User.objects.get(id=ususario_id)
    propiedad = Propiedad.objects.get(id=propiedad_id)

    new_venta = Venta.objects.new_venta(agente, ususario, propiedad)

    propiedad.sold_out = True
    propiedad.save()

    messages.success(request, 'Operacion realizada con éxito. Nuestro agente se pondrá en contacto contigo. Muchas gracias!')

    return redirect('core:home')

def VentaCancel(request, pk):
    
    venta = Venta.objects.get(id=pk)
    propiedad = Propiedad.objects.get(id=venta.propiedad.id)

    propiedad.sold_out = False

    propiedad.save()

    venta.delete()
    
    messages.success(request, 'Compra cancelada con éxito')

    return redirect ('/')
