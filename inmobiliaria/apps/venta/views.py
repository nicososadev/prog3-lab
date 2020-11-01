from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .models import Venta
from apps.propiedad.models import Propiedad
from apps.agente.models import Agente

User = get_user_model()


def VentaListView(request):
    pass

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

    return redirect('core:home')
