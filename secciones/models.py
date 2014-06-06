# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

class TipoSeccion(models.Model):
    nombre = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    
    class Meta:
        verbose_name = 'Tipo Sección'
        verbose_name_plural = 'Tipos de Secciones'
    
    def __unicode__(self):
        return self.nombre

    def save(self):
        self.slug = slugify(self.nombre)
        super(TipoSeccion,self).save()

class Seccion(models.Model):
    tipo = models.ForeignKey(TipoSeccion)
    titulo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='foto_seccion', blank=False, max_length=200)    
    contenido = models.TextField(blank=False)
    fechaCreacion = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'
    
    def __unicode__(self):
        return self.titulo

    def save(self):
        self.slug = slugify(self.titulo)
        super(Seccion,self).save()