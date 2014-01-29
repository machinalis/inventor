# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Part.part_for_sale'
        db.add_column('stock_part', 'part_for_sale',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Part.part_price'
        db.add_column('stock_part', 'part_price',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Part.part_for_sale'
        db.delete_column('stock_part', 'part_for_sale')

        # Deleting field 'Part.part_price'
        db.delete_column('stock_part', 'part_price')


    models = {
        'stock.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'stock.part': {
            'Meta': {'object_name': 'Part'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.Brand']"}),
            'part_for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'part_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.Station']", 'null': 'True', 'blank': 'True'}),
            'part_physical_identifier': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'part_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'part_spec': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'part_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.PartState']", 'null': 'True', 'blank': 'True'}),
            'part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.PartType']"}),
            'reference_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'stock.partstate': {
            'Meta': {'object_name': 'PartState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_is_usable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'stock.parttype': {
            'Meta': {'object_name': 'PartType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'stock.physicallocation': {
            'Meta': {'object_name': 'PhysicalLocation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'stock.station': {
            'Meta': {'object_name': 'Station'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_owner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'physical_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.PhysicalLocation']", 'null': 'True', 'blank': 'True'}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['stock']