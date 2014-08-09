# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReportPDF'
        db.create_table(u'maps_reportpdf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pdf_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'maps', ['ReportPDF'])


    def backwards(self, orm):
        # Deleting model 'ReportPDF'
        db.delete_table(u'maps_reportpdf')


    models = {
        u'maps.reportpdf': {
            'Meta': {'object_name': 'ReportPDF'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['maps']