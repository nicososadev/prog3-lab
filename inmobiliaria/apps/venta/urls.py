from django.urls import path

from . import views

app_name = 'venta'

urlpatterns = [
    path('confirmar/', views.VentaConfirm, name='confirmar-venta'),
    path('compras/', views.VentasList, name='vendidas'),
    path('compras/<int:pk>', views.VentaCancel, name='cancel')
]