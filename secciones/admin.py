# -*- coding: utf-8 -*-
from django.contrib import admin
from secciones.models import TipoSeccion, Seccion

class SeccionAdmin(admin.ModelAdmin):    
    exclude = ('slug',)

class TipoSeccionAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(TipoSeccion,TipoSeccionAdmin)
admin.site.register(Seccion,SeccionAdmin)