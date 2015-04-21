from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noticias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^inicio/$', 'sitio.views.inicio'),
    url(r'^novedades/$', 'sitio.views.novedades'),

    url(r'^contador_ajax/$', 'sitio.views.contador_ajax',
        name='contador_ajax'),
    url(r'^titulos_noticias/$', 'sitio.views.titulos_noticias',
        name='titulos_noticias'),

    url(r'^admin/', include(admin.site.urls)),
)
