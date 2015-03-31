# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Noticia.copete'
        db.add_column(u'sitio_noticia', 'copete',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Noticia.copete'
        db.delete_column(u'sitio_noticia', 'copete')


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
            'copete': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sitio']