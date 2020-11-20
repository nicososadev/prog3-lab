from django.urls import path

from . import views

app_name = 'propiedad'

urlpatterns = [
    path('', views.propiedadList, name='list'),
    path('detail/<int:propiedad_id>/', views.propiedadDetail, name='detail'),
    path('registar-propiedad/', views.propiedadCreate, name='registrar'),
    path('actualizar-propiedad/<int:propiedad_id>/', views.propiedadUpdate, name='actualizar'),
    path('eliminar-propiedad/<int:propiedad_id>/', views.propiedadDeleteConfirm, name='confirmar'),
    path('confirmar-eliminar-propiedad/<int:propiedad_id>/', views.propiedadDelete, name='eliminar'),
    path('filter/', views.propiedadListFilter, name='filter'),
]