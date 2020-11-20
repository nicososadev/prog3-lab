from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .models import Agente
from apps.propiedad.models import Propiedad
from apps.user.decorators import allowed_users

@login_required(login_url='/users/login/')
@allowed_users(allowed_roles=['agente'])
def propiedadesAgente(request):

    user = request.user

    try:
        # agente = Agente.objects.get(user=user)
        propiedades = Propiedad.objects.filter(agente=user)
    except ObjectDoesNotExist:
        messages.error(request, 'Hubo un problema listando las propiedades')
        return redirect('core:home')

    context = {
        'propiedades': propiedades
    }

    return render(request, 'agente/propiedad-agente-list.html', context)