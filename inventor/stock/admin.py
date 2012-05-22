# -*- coding: utf-8 -*-
from django.contrib import admin

from stock.models import Brand, PartType, PartState, PhysicalLocation, Station, Part

class BrandAdmin(admin.ModelAdmin):
   list_display = ('name',) 

admin.site.register(Brand, BrandAdmin)

class PartTypeAdmin(admin.ModelAdmin):
    list_display = ('name',) 

admin.site.register(PartType, PartTypeAdmin)

class PartStateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'state_is_usable')
    list_filter = ('state_is_usable',)

admin.site.register(PartState, PartStateAdmin)

class PhysicalLocationAdmin(admin.ModelAdmin):
    list_display = ('name',) 

admin.site.register(PhysicalLocation, PhysicalLocationAdmin)

class PartAdmin(admin.ModelAdmin):
    list_display = ('part_brand', 'part_spec', 'part_state', 'part_location')
    search_fields = ('part_type', 'part_brand', 'part_spec', 'part_location')
    list_filter = ('part_type', 'part_brand', 'part_location', 'part_state')

class InlinePartAdmin(admin.TabularInline):
    model = Part

admin.site.register(Part, PartAdmin)

class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'physical_location', 'location_owner')
    list_filter = ('physical_location', ) 
    inlines = (InlinePartAdmin, )

admin.site.register(Station, StationAdmin)


