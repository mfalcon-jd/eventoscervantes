# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventoscervantes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'secciones.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacto/$', 'secciones.views.contacto', name='contacto'),
    # url(r'^pagina/', include('secciones.urls')),
    url(r'^seccion/(?P<slug>[a-zA-Z0-9\-]+)/$', 'secciones.views.seccion', name='seccion'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)/$', 'secciones.views.pagina', name='pagina'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
