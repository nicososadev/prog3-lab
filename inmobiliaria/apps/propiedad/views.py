from django.shortcuts import render

def propiedadDetail(request):
    
    return render(request, 'propiedad-detail.html', {})

def propiedadList(request):

    return render(request, 'propiedad-list.html', {})

def propiedadCreate(request):

    return render(request, 'propiedad-form.html', {})  
