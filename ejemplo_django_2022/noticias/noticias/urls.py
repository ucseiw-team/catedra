"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from sitio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('api/contador_noticias_html/', views.contador_noticias_html),
    path('api/contador_noticias_json/', views.contador_noticias_json),
    path('ejemplo_form_pelado/', views.ejemplo_form_pelado),
    path('ejemplo_form_django/', views.ejemplo_form_django),
    path('ejemplo_model_form_django/', views.ejemplo_model_form_django),
    path('search/', include('haystack.urls')),
]
