# -*- coding: utf-8 -*-
from django.contrib import admin

from stock.models import Brand, PartType, PartState, PhysicalLocation,Station, Part
from django.forms import ModelForm


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


class PartAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartAdminForm, self).__init__(*args, **kwargs)
        self.fields['part_container'].queryset = Part.objects.filter(
            part_is_container=True)


class PartAdmin(admin.ModelAdmin):
    form = PartAdminForm
    list_display = ('part_brand', 'part_spec', 'part_state', 'part_location',
        'part_is_container', 'is_empty')
    search_fields = ('part_type', 'part_brand', 'part_spec', 'part_location')
    list_filter = ('part_type', 'part_brand', 'part_location',
        'part_state', 'part_is_container')

admin.site.register(Part, PartAdmin)


class InlinePartAdmin(admin.TabularInline):
    model = Part


class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'physical_location', 'location_owner')
    list_filter = ('physical_location', )
    inlines = (InlinePartAdmin, )

admin.site.register(Station, StationAdmin)


