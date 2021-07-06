"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from typing import KeysView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # path del Core
    path('', include('core.urls')),

    # path del Services
    path('services/', include('services.urls')),
    
    # path del Blog
    path('blog/', include('blog.urls')),

    # path del Pages
    path('page/', include('pages.urls')),

    # path del Contacto
    path('contact/', include('contact.urls')),

    # path del Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:              # agregado para poder visualizar por ejemplo Imagenes en un entorno de desarrollo
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Custom titiles for admin
admin.site.site_header = "La Caffetiera"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "La Caffetiera"
