from django.shortcuts import render

def HomePage(request):

    return render(request, 'homepage.html', {})

def ContactView(request):
        
    return render(request, 'contact/contact.html', {})

def LoginView(request):
    
    return render(request, 'auth/login.html', {})

def RegisterView(request):
    
    return render(request, 'auth/register.html', {})