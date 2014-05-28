# -*- coding: utf-8 -*-
from django.db import models

class Galeria(models.Model):
	nombre = models.CharField(max_length=150, blank=False, null=False)
	fecha = models.DateField(blank=False)
	descripcion = models.TextField(blank=True, null=True)
	carousel = models.BooleanField(default=False)
	fechaCreacion = models.DateField(auto_now_add=True)
	slug = models.SlugField(max_length=100)
	
	class Meta:
		verbose_name = 'Galería'
		verbose_name_plural = 'Galerías'

	def __unicode__(self):
		return self.nombre

class Imagen(models.Model):
	galeria = models.ForeignKey(Galeria)
	titulo = models.CharField(max_length=150, blank=True, null=True)
	imagen = models.ImageField(upload_to='galeria', blank=False, max_length=250)

	class Meta:
		verbose_name = 'Imagen'
		verbose_name_plural = 'Imagenes'

	def __unicode__(self):
		return self.titulo