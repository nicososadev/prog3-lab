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

from . import views

urlpatterns = [
    # Jet
    path('jet/', include('jet.urls', 'jet')),

    # Admin
    path('admin/', admin.site.urls),

    # App
    path('', views.HomePage, name='home'),
    path('contact/', views.ContactView, name='contact'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),

    # Propiedad
    path('propiedad/', include('apps.propiedad.urls', namespace='propiedad')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
