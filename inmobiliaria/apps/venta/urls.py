from django.urls import path

from . import views

app_name = 'venta'

urlpatterns = [
    path('detalle/<int:propiedad_id>', views.VentaDetail, name='detalle-venta'),
    path('confirmar/<int:propiedad_id>', views.VentaConfirm, name='confirmar-venta'),
    path('completar/<int:venta_id>', views.VentaCompleted, name='completar-venta'),
    path('compras/', views.ComprasList, name='compras'),
    path('ventas/', views.VentasList, name='ventas'),
    path('completadas/', views.VentasCompletedList, name='ventas-completadas'),
    path('compras/<int:pk>', views.VentaCancel, name='cancel')
]