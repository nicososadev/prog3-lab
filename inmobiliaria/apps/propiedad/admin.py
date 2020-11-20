from django.contrib import admin

from .models import Propiedad

class PropiedadAdmin(admin.ModelAdmin):
    readonly_fields = ('reserved', 'created', 'updated')
    list_display = ('id', 'propType', 'operation','agente', 'featured', 'reserved' , 'precio')
    list_filter = ('propType', 'operation')

admin.site.register(Propiedad, PropiedadAdmin)
