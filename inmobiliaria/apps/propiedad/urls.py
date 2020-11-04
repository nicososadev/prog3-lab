from django.urls import path

from . import views

app_name = 'propiedad'

urlpatterns = [
    path('', views.propiedadList, name='list'),
    path('detail/<int:propiedad_id>/', views.propiedadDetail, name='detail'),
    path('registar-propiedad/', views.propiedadCreate, name='registrar'),
    path('filter/', views.propiedadListFilter, name='filter'),
]