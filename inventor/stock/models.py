from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(u"Brand Name", max_length=100)

class PartType(models.Model):
    name = models.CharField(u"Part Type", max_length=100, help_text=u"Such as Hard Drive or Printer")

class PartState(models.Model):
    state_name = models.CharField(u"State denomination", max_length=100, help_text=u"such as broken or in repair")
    state_is_usable = models.BooleanField(u"Can be used in this state?")

class PhysicalLocation(models.Model):
    name = models.CharField(u"Name of the place", max_length=100, help_text=u"What do we name this place")
    description = models.CharField(u"Location Description", max_length=255, help_text=u"Where is this, for instance, the kitchen")

class Station(models.Model):
    station_name = models.CharField(u"Name the location", max_length=100, help_text=u"Typically a workstation, use the"
                                                                                    "hostname if any")
    physical_location = models.ForeignKey(PhysicalLocation)
    location_owner = models.CharField(u"Who is responsable for this", max_length=100, help_text=u"Just the name")

class Part(models.Model):
    part_type = models.ForeignKey(u"Part Type", PartType)
    part_brand = models.ForeignKey(u"Brand", Brand)
    part_spec = models.CharField(u"Specs", max_length=255, help_text=u"Specs can be more identifying traces, such as 1G,
    Sata, etc. for Hard Drives")
    reference_url = models.URLField(u"Reference URL", help_text=u"A URL with info regarding the part, manufacturer one
    is prefered")
    part_state = models.ForeignKey(u"State of this part", PartState)
    part_location = models.ForeignKey(u"Where is this?", Station, help_text=u"Typically a workstation")
