from django.urls import path

from . import views

app_name = 'agente'

urlpatterns = [
    path('propiedades/', views.propiedadesAgente, name='propiedades')
]