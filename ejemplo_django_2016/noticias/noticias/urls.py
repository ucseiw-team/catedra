"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^inicio/$', 'sitio.views.inicio'),
    url(r'^inicio_ajax/$', 'sitio.views.inicio_ajax'),
    url(r'^lista_noticias_ajax/$', 'sitio.views.lista_noticias_ajax', name="lista_noticias_ajax"),
    url(r'^contador_noticias_ajax/$', 'sitio.views.contador_noticias_ajax', name="contador_noticias_ajax"),
    url(r'^pedir_datos/$', 'sitio.views.pedir_datos'),
    url(r'^admin/', include(admin.site.urls)),
]





