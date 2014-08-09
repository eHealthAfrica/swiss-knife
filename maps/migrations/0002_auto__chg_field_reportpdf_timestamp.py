# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ReportPDF.timestamp'
        db.alter_column(u'maps_reportpdf', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'ReportPDF.timestamp'
        db.alter_column(u'maps_reportpdf', 'timestamp', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'maps.reportpdf': {
            'Meta': {'object_name': 'ReportPDF'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maps']