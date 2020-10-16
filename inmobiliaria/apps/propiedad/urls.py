from django.contrib import admin
from django.urls import path

from . import views

app_name = 'propiedad'

urlpatterns = [

    path('', views.propiedadList, name='list'),
    path('detail/', views.propiedadDetail, name='detail'),
    path('registar-propiedad/', views.propiedadCreate, name='registrar'),
]