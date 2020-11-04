from django.contrib import admin

from .models import Venta

class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('id', 'agente', 'usuario','propiedad')

admin.site.register(Venta, VentaAdmin)
