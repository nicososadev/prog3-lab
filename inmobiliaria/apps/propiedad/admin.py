from django.contrib import admin

from .models import Propiedad

class PropiedadAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'propType', 'operation','agente' , 'precio')
    list_filter = ('propType', 'operation')

admin.site.register(Propiedad, PropiedadAdmin)
