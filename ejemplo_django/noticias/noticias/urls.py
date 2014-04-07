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

    url(r'^admin/', include(admin.site.urls)),
)
