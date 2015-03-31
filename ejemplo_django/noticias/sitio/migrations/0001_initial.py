# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'sitio_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'sitio', ['Categoria'])

        # Adding model 'Noticia'
        db.create_table(u'sitio_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
            ('archivada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitio.Categoria'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sitio', ['Noticia'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'sitio_categoria')

        # Deleting model 'Noticia'
        db.delete_table(u'sitio_noticia')


    models = {
        u'sitio.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sitio.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'archivada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sitio.Categoria']", 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sitio']