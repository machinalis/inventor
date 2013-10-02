# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table('stock_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('stock', ['Brand'])

        # Adding model 'PartType'
        db.create_table('stock_parttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('stock', ['PartType'])

        # Adding model 'PartState'
        db.create_table('stock_partstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state_is_usable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('stock', ['PartState'])

        # Adding model 'PhysicalLocation'
        db.create_table('stock_physicallocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('stock', ['PhysicalLocation'])

        # Adding model 'Station'
        db.create_table('stock_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('physical_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.PhysicalLocation'], null=True, blank=True)),
            ('location_owner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('stock', ['Station'])

        # Adding model 'Part'
        db.create_table('stock_part', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.PartType'])),
            ('part_brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.Brand'])),
            ('part_spec', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reference_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('part_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.PartState'], null=True, blank=True)),
            ('part_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.Station'], null=True, blank=True)),
            ('part_physical_identifier', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('stock', ['Part'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table('stock_brand')

        # Deleting model 'PartType'
        db.delete_table('stock_parttype')

        # Deleting model 'PartState'
        db.delete_table('stock_partstate')

        # Deleting model 'PhysicalLocation'
        db.delete_table('stock_physicallocation')

        # Deleting model 'Station'
        db.delete_table('stock_station')

        # Deleting model 'Part'
        db.delete_table('stock_part')


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
            'part_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.Station']", 'null': 'True', 'blank': 'True'}),
            'part_physical_identifier': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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