# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('secciones.views',
    url(r'(?P<slug>[a-zA-Z0-9\-]+)/$', 'tipo_seccion', name='tipo_seccion'),
)