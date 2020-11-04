from django.contrib import admin

from .models import Propiedad

class PropiedadAdmin(admin.ModelAdmin):
    readonly_fields = ('sold_out', 'created', 'updated')
    list_display = ('id', 'propType', 'operation','agente', 'sold_out' , 'precio')
    list_filter = ('propType', 'operation')

admin.site.register(Propiedad, PropiedadAdmin)
