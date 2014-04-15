from django.conf.urls import patterns, include, url

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

    url(r'^admin/', include(admin.site.urls)),
)
