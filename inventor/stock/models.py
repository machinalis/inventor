from django.db import models
from django.core.exceptions import ValidationError


class Brand(models.Model):
    """The brand of the part"""
    name = models.CharField(u"Brand Name", max_length=100)

    def __unicode__(self):
        return self.name


class PartType(models.Model):
    """The part type such as 'hard drive' or 'printer'"""
    name = models.CharField(u"Part Type", max_length=100,
        help_text=u"Such as Hard Drive or Printer")

    def __unicode__(self):
        return self.name


class PartState(models.Model):
    """The state of the item such as 'broken' or 'in repair'"""
    state_name = models.CharField(u"State denomination", max_length=100,
        help_text=u"such as broken or in repair")
    state_is_usable = models.BooleanField(u"Can be used in this state?")

    def __unicode__(self):
        usable = self.state_is_usable and "usable" or "not usable"
        return u"%s (%s)" % (self.state_name, usable)


class PhysicalLocation(models.Model):
    """The physical location of the item such as 'the kitchen' or
    'meeting room #1'"""
    name = models.CharField(u"Name of the place", max_length=100,
        help_text=u"What do we name this place")
    description = models.CharField(u"Location Description", max_length=255,
        help_text=u"Where is this, for instance, "
    "the kitchen", blank=True, null=True)

    def __unicode__(self):
        return self.name


class Station(models.Model):
    """The station in which the part currently resides"""
    station_name = models.CharField(u"Name the location", max_length=100,
        help_text=u"Typically a workstation, use the hostname if any")
    physical_location = models.ForeignKey(PhysicalLocation, blank=True,
        null=True)
    location_owner = models.CharField(u"Who is responsable for this",
        max_length=100, help_text=u"Just the name",
    blank=True, null=True)

    def __unicode__(self):
        return u"%s @ %s (%s)" % (self.station_name, self.physical_location,
            self.location_owner)


def validate_is_container(pk):
    """Validates whether the entity is a container"""
    part = Part.objects.get(pk=pk)

    if not part.part_is_container:
        raise ValidationError(u"%s is not a container" % part)


class Part(models.Model):
    """An inventory item"""
    part_type = models.ForeignKey(PartType, verbose_name=u"Part type")
    part_brand = models.ForeignKey(Brand, verbose_name=u"Brand")
    part_spec = models.CharField(u"Specs", max_length=255,
        help_text=u"Specs can be more identifying traces, such as 1G,"
    "Sata, etc. for Hard Drives", blank=True, null=True)
    reference_url = models.URLField(u"Reference URL",
        help_text=u"A URL with info regarding the part, manufacturer one "
        "is prefered", blank=True, null=True)
    part_state = models.ForeignKey(PartState, verbose_name=u"State of this "
        "part", blank=True, null=True)
    part_location = models.ForeignKey(Station, verbose_name=u"Where is this?",
        help_text=u"Typically a workstation", blank=True, null=True)
    part_physical_identifier = models.CharField(u"Physical identifier",
        max_length=100, help_text=u"The text on the label",
        blank=True, null=True)
    part_for_sale = models.BooleanField(u"For sale?", help_text=u"Whether the "
        "part is up for sale")
    part_price = models.DecimalField(u"Price", max_digits=10, decimal_places=2,
        blank=True, null=True, help_text=u"The selling price for the part")
    part_is_container = models.BooleanField(u"Is a container?",
        help_text=u"Whether the part is a container of other parts")
    part_container = models.ForeignKey('self', related_name='contained',
        blank=True, null=True, help_text=u"The container that holds this part",
        validators=[validate_is_container])

    def is_empty(self):
        """Returns whether the container is empty"""
        return self.contained.count() == 0

    is_empty.admin_order_field = 'part_brand'
    is_empty.boolean = True
    is_empty.short_description = 'Is empty?'

    def __unicode__(self):
        return u"%s %s %s @ %s (%s)" % (self.part_type, self.part_brand,
            self.part_spec, self.part_location, self.part_state)
