from django.contrib import admin
from django.urls import path

from . import views

app_name = 'propiedad'

urlpatterns = [

    path('detail/', views.propiedadDetail, name='detail'),
]