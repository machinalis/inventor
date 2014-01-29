# -*- coding: utf-8 -*-
from django.contrib import admin
from stock.models import Brand, PartType, PartState, PhysicalLocation,\
    Station, Part
from forms import PartAdminForm, StationAdminForm
from django.core.urlresolvers import reverse

ITEM_QUANTITY = 15


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_per_page = ITEM_QUANTITY


class PartTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_per_page = ITEM_QUANTITY


class PartStateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'state_is_usable')
    list_filter = ('state_is_usable',)
    ordering = ('state_name',)
    list_per_page = ITEM_QUANTITY


class PhysicalLocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_per_page = ITEM_QUANTITY


class PartAdmin(admin.ModelAdmin):
    form = PartAdminForm
    list_display = ('part_type', 'part_brand', 'part_spec', 'part_state',
                    'where_is_method', 'part_is_container', 'part_set_method')
    search_fields = ('part_type', 'part_brand', 'part_spec', 'part_location')
    list_filter = ('part_type', 'part_brand', 'part_location',
                   'part_state', 'part_is_container')
    list_select_related = ('part_type', 'part_brand',
                           'part_spec', 'part_location',
                           'part_state')
    exclude = ('part_container', )
    ordering = ('part_type__name',)
    list_per_page = ITEM_QUANTITY

    def part_set_method(self, obj):
        if obj.part_is_container:
            parts = obj.contained.all().select_related('part_type__name',
                                                       'part_brand__name',
                                                       'part_spec__name',
                                                       'part_location__name',
                                                       'part_state')
            li = ""
            result = "<ul>%s</ul>"
            for part in parts:
                li = li + '<li><a href="%s">%s</a></li>'\
                    % (reverse('admin:stock_part_change', args=[part.pk]),
                       part)
            return result % li
        else:
            return ""
    part_set_method.short_description = 'Parts Contained'
    part_set_method.allow_tags = True

    def where_is_method(self, obj):
        result = '<a href="%s">%s</a>'\
            % (reverse('admin:stock_station_change',
                       args=[obj.part_location_id]), obj.part_location)
        return result
    where_is_method.short_description = 'Where_is this?'
    where_is_method.allow_tags = True

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if change:
                obj.contained.clear()
            obj.save()
            for part in form.cleaned_data['parts']:
                obj.contained.add(part)
                obj.save()

    def delete_model(self, request, obj):
        if obj.contained:
            obj.contained.clear()
        obj.delete()


class InlinePartAdmin(admin.TabularInline):
    model = Part
    #Not show "Add another part"
    max_num = 0
    fields = ('part_type', 'part_brand', 'part_spec', 'part_state',
              'part_location', 'part_physical_identifier', 'part_for_sale',
              'part_price', 'part_is_container',)
    readonly_fields = ('part_type', 'part_brand', 'part_spec',
                       'part_state', 'part_location',
                       'part_physical_identifier', 'part_for_sale',
                       'part_price', 'part_is_container', 'is_empty',)
    exclude = ('part_container', )


class StationAdmin(admin.ModelAdmin):
    form = StationAdminForm
    list_display = ('station_name', 'physical_location', 'location_owner',
                    'part_set_method')
    list_filter = ('physical_location', )
    list_select_related = ('part_type__name', 'part_brand__name',
                           'part_spec__name', 'part_location__name',
                           'part_state')
    ordering = ('station_name', )
    inlines = (InlinePartAdmin, )
    list_per_page = 3

    def part_set_method(self, obj):
        parts = obj.part_set.all().select_related('part_type__name',
                                                  'part_brand__name',
                                                  'part_spec__name',
                                                  'part_location__name',
                                                  'part_state')
        li = ""
        if parts:
            result = "<ul>%s</ul>"
            for part in parts:
                li = li + '<li><a href="%s">%s</a></li>'\
                    % (reverse('admin:stock_part_change', args=[part.pk]),
                       part)
            return result % li
        else:
            return "Empty Station"
    part_set_method.short_description = 'Station Elements'
    part_set_method.allow_tags = True


admin.site.register(Brand, BrandAdmin)
admin.site.register(PartType, PartTypeAdmin)
admin.site.register(PartState, PartStateAdmin)
admin.site.register(PhysicalLocation, PhysicalLocationAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Station, StationAdmin)
