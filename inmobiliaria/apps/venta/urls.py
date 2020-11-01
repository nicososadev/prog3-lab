from django.urls import path

from . import views

app_name = 'venta'

urlpatterns = [
    path('confirmar/', views.VentaConfirm, name='confirmar-venta')
]