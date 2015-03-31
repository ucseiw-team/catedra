from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noticias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^inicio/$', 'sitio.views.inicio'),

    url(r'^admin/', include(admin.site.urls)),
)
