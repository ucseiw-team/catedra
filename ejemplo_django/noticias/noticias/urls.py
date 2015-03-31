from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noticias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^inicio/$', 'sitio.views.inicio', name='inicio'),

    url(r'^contador/$', 'sitio.views.contador', name='contador'),
    url(r'^vacia/$', 'sitio.views.vacia', name='vacia'),

    url(r'^contador_ajax/$', 'sitio.views.contador_ajax', name='contador_ajax'),
    url(r'^sumar_numero/(\d+)/$', 'sitio.views.sumar_numero', name='sumar_numero'),
    url(r'^sumar_numero_json/(\d+)/$', 'sitio.views.sumar_numero_json', name='sumar_numero_json'),

    url(r'^crear_policial/$', 'sitio.views.crear_noticia_policial', name='crear_policial'),

    url(r'^crear_noticia_con_datos/$', 'sitio.views.crear_noticia_con_datos', name='sitio.views.crear_noticia_con_datos'),

    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^search/', include('haystack.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
