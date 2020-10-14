from django.shortcuts import render

def propiedadDetail(request):
    
    return render(request, 'propiedad/propiedad-detail.html', {})
