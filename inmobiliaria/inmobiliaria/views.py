from django.shortcuts import render

from apps.propiedad.models import Propiedad

def HomePage(request):

    propiedades = Propiedad.objects.all()
    context = {
        'propiedades': propiedades
    }
    return render(request, 'homepage.html', context)

def ContactView(request):
        
    return render(request, 'contact/contact.html', {})

def LoginView(request):
    
    return render(request, 'auth/login.html', {})

def RegisterView(request):
    
    return render(request, 'auth/register.html', {})