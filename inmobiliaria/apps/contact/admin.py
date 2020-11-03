from django.contrib import admin

from .models import Mensaje

class MensajeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'email', 'created')

admin.site.register(Mensaje, MensajeAdmin)
