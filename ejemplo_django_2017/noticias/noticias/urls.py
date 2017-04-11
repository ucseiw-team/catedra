"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from sitio.views import inicio, login_fake, crear_noticia, lista_noticias_ajax, contador_noticias_ajax, acerca_de

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/$', inicio),
    url(r'^acerca_de/$', acerca_de),
    url(r'^login_fake/$', login_fake),
    url(r'^crear_noticia/$', crear_noticia),
    url(r'^lista_noticias_ajax/$', lista_noticias_ajax),
    url(r'^contador_noticias_ajax/$', contador_noticias_ajax),
]
