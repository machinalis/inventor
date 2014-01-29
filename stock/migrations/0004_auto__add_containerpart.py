# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContainerPart'
        db.create_table(u'stock_containerpart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cointaner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.Part'], null=True, blank=True)),
        ))
        db.send_create_signal(u'stock', ['ContainerPart'])


    def backwards(self, orm):
        # Deleting model 'ContainerPart'
        db.delete_table(u'stock_containerpart')


    models = {
        u'stock.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stock.containerpart': {
            'Meta': {'object_name': 'ContainerPart'},
            'cointaner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.Part']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stock.part': {
            'Meta': {'object_name': 'Part'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.Brand']"}),
            'part_container': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contained'", 'null': 'True', 'to': u"orm['stock.Part']"}),
            'part_for_sale': ('django.db.models.fields.BooleanField', [], {}),
            'part_is_container': ('django.db.models.fields.BooleanField', [], {}),
            'part_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.Station']", 'null': 'True', 'blank': 'True'}),
            'part_physical_identifier': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'part_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'part_spec': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'part_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.PartState']", 'null': 'True', 'blank': 'True'}),
            'part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.PartType']"}),
            'reference_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'stock.partstate': {
            'Meta': {'object_name': 'PartState'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_is_usable': ('django.db.models.fields.BooleanField', [], {}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stock.parttype': {
            'Meta': {'object_name': 'PartType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stock.physicallocation': {
            'Meta': {'object_name': 'PhysicalLocation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stock.station': {
            'Meta': {'object_name': 'Station'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_owner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'physical_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.PhysicalLocation']", 'null': 'True', 'blank': 'True'}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['stock']