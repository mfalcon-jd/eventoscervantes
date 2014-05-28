# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Galeria'
        db.create_table(u'galerias_galeria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'galerias', ['Galeria'])

        # Adding model 'Imagen'
        db.create_table(u'galerias_imagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['galerias.Galeria'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=250)),
        ))
        db.send_create_signal(u'galerias', ['Imagen'])


    def backwards(self, orm):
        # Deleting model 'Galeria'
        db.delete_table(u'galerias_galeria')

        # Deleting model 'Imagen'
        db.delete_table(u'galerias_imagen')


    models = {
        u'galerias.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'galerias.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['galerias.Galeria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['galerias']