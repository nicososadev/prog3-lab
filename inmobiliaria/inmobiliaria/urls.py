"""Inmobiliaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Jet
    path('jet/', include('jet.urls', 'jet')),

    # Admin
    path('admin/', admin.site.urls),

    # Core
    path('', include('apps.core.urls', namespace='core')),

    # Users
    path('users/', include('apps.user.urls', namespace='user')),

    # Propiedad
    path('propiedad/', include('apps.propiedad.urls', namespace='propiedad')),

    # Contact
    path('contact/', include('apps.contact.urls', namespace='contact')),

    # Venta
    path('venta/', include('apps.venta.urls', namespace='venta')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
