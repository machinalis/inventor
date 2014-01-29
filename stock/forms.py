from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from stock.models import Part, Station


class PartAdminForm(ModelForm):
    qry = Part.objects.filter(part_is_container=False,
                              part_state__state_is_usable=True).select_related(
                                  'part_type__name', 'part_brand__name',
                                  'part_spec__name', 'part_location__name',
                                  'part_state').order_by('part_type__name')
    parts = ModelMultipleChoiceField(queryset=qry,
                                     required=False,
                                     widget=FilteredSelectMultiple('Part',
                                                                   False))

    def __init__(self, *args, **kwargs):
        super(PartAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['parts'] = self.instance.contained.all().order_by(
                'part_type__name')
        self.fields['part_state'].required = True
        self.fields['part_location'].required = True
        self.fields['part_physical_identifier'].required = True

    class Meta:
        model = Part
        exclude = ('part_container',)

    def clean_parts(self):
        parts = self.cleaned_data.get('parts')
        is_container = self.cleaned_data.get('part_is_container')
        if parts and not is_container:
            raise forms.ValidationError(u'Some parts and is not a container')
        if not parts and is_container:
            raise forms.ValidationError(u'Is a container without parts')
        if parts and is_container:
            for part in parts:
                if part.part_container:
                    raise forms.ValidationError(u'%s it is another container'
                                                % part)
        return parts


class StationAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StationAdminForm, self).__init__(*args, **kwargs)
        self.fields['location_owner'].required = True

    class Meta:
        model = Station
