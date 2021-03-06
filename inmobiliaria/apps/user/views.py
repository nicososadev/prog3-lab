from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model

from .forms import LoginForm, RegisterForm

def LoginView(request):
    form = LoginForm(request.POST or None)
    
    context = {
        'form': form
    }

    next_ = request.GET.get('next') or None
    
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,'Te has logeado con éxito')
                if next_ is not None:
                    return redirect(next_)
                return redirect('/')
            else:
                messages.error(request,'Email o contraseña incorrectos')

    return render(request, 'user/login.html', context)

def LogoutView(request):
    logout(request)
    messages.success(request,'Te has deslogeado con éxito')
    return redirect('/')

User = get_user_model()
def RegisterView(request):
    form = RegisterForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        
        new_user = User.objects.create_user(name, email, password)

        if new_user is not None:
            login(request, new_user)
            messages.success(request,'Te has registrado con éxito')
            return redirect('/')

        else:
            print('Authenticate Error')

    return render(request, 'user/register.html', context)
