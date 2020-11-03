from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ContactFrom

def ContactView(request):
    
    form = ContactFrom(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        form.save()
        messages.success(request, 'Hemos recibido tu mensaje. Te responderemos en cuanto lo leamos.')
        return redirect('contact:contact')

    return render(request, 'contact/contact.html', context)
