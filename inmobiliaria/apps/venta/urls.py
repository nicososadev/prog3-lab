from django.urls import path

from . import views

app_name = 'venta'

urlpatterns = [
    path('detalle/<int:propiedad_id>', views.VentaDetail, name='detalle-venta'),
    path('confirmar/<int:propiedad_id>', views.VentaConfirm, name='confirmar-venta'),
    path('compras/', views.ComprasList, name='compras'),
    path('ventas/', views.VentasList, name='ventas'),
    path('compras/<int:pk>', views.VentaCancel, name='cancel')
]