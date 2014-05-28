# -*- coding: utf-8 -*-
from django.contrib import admin
from galerias.models import Galeria, Imagen

class ImagenInline(admin.TabularInline):
	model = Imagen
	extra = 3

class GaleriaAdmin(admin.ModelAdmin):
	"""docstring for Galeria"""
	inlines = [ImagenInline]

admin.site.register(Galeria, GaleriaAdmin)