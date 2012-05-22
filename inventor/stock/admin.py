# -*- coding: utf-8 -*-
from django.contrib import admin

from stock.model import Brand, PartType, PartState, PhysicalLocation, Station, Part

class BrandAdmin(admin.ModelAdmin):
   list_display = ('name',) 

admin.site.register(Brand, BrandAdmin)

class PartTypeAdmin(admin.ModelAdmin)
    list_display = ('name',) 

admin.site.register(PartType, PartTypeAdmin)

class PartStateAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_usable')
    filter_horizontal = ('is_usable',)

admin.site.register(PartType, PartTypeAdmin)

class PhysicalLocationAdmin(admin.ModelAdmin):
    list_display = ('name',) 

admin.site.register(PartType, PartTypeAdmin)

class PartAdmin(admin.ModelAdmin):
    list_display = ('part_type', 'part_brand', 'part_spec', 'part_state', 'part_location')
    search_fields = ('part_type', 'part_brand', 'part_spec', 'part_location')
    filter_horizontal = ('part_type', 'part_brand', 'part_location', 'part_state')

class InlinePartAdmin(admin.TabularInline):
    model = Part

admin.site.register(PartType, PartTypeAdmin)

class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'physical_location', 'location_owner')
    filter_horizontal = ('physical_location', ) 
    inlines = (InlinePartAdmin, )

admin.site.register(PartType, PartTypeAdmin)


