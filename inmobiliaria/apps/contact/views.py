from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactFrom

def ContactView(request):
    
    form = ContactFrom(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/")

    return render(request, 'contact/contact.html', context)
