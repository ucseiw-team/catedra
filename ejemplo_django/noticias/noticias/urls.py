from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noticias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ejemplo_clase_1/$', 'sitio.views.ejemplo_clase_1', name='ejemplo_clase_1'),
    url(r'^ejemplo_clase_2/$', 'sitio.views.ejemplo_clase_2', name='ejemplo_clase_2'),

    url(r'^admin/', include(admin.site.urls)),
)
