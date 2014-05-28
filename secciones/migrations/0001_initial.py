# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoSeccion'
        db.create_table(u'secciones_tiposeccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'secciones', ['TipoSeccion'])

        # Adding model 'Seccion'
        db.create_table(u'secciones_seccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['secciones.TipoSeccion'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=200)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('fechaCreacion', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'secciones', ['Seccion'])


    def backwards(self, orm):
        # Deleting model 'TipoSeccion'
        db.delete_table(u'secciones_tiposeccion')

        # Deleting model 'Seccion'
        db.delete_table(u'secciones_seccion')


    models = {
        u'secciones.seccion': {
            'Meta': {'object_name': 'Seccion'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fechaCreacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['secciones.TipoSeccion']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'secciones.tiposeccion': {
            'Meta': {'object_name': 'TipoSeccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['secciones']