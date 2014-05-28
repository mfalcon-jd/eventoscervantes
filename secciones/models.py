# -*- coding: utf-8 -*-
from django.db import models

class TipoSeccion(models.Model):
    nombre = models.CharField(max_length=80)
    
    class Meta:
        verbose_name = 'Tipo Sección'
        verbose_name_plural = 'Tipos de Secciones'
    
    def __unicode__(self):
        return self.nombre

class Seccion(models.Model):
    tipo = models.ForeignKey(TipoSeccion)
    titulo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='foto_seccion', blank=False, max_length=200)    
    contenido = models.TextField(blank=False)
    fechaCreacion = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'
    
    def __unicode__(self):
        return self.titulo