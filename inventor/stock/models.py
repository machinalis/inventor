from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(u"Brand Name", max_length=100)

    def __unicode__(self):
        return self.name

class PartType(models.Model):
    name = models.CharField(u"Part Type", max_length=100, help_text=u"Such as Hard Drive or Printer")

    def __unicode__(self):
        return self.name

class PartState(models.Model):
    state_name = models.CharField(u"State denomination", max_length=100, help_text=u"such as broken or in repair")
    state_is_usable = models.BooleanField(u"Can be used in this state?")

    def __unicode__(self):
        usable = self.state_is_usable and "usable" or "not usable"
        return u"%s (%s)" % (self.state_name, usable)

class PhysicalLocation(models.Model):
    name = models.CharField(u"Name of the place", max_length=100, help_text=u"What do we name this place")
    description = models.CharField(u"Location Description", max_length=255, help_text=u"Where is this, for instance, "
    "the kitchen", blank=True, null=True)

    def __unicode__(self):
        return self.name

class Station(models.Model):
    station_name = models.CharField(u"Name the location", max_length=100, help_text=u"Typically a workstation, use the"
                                                                                    "hostname if any")
    physical_location = models.ForeignKey(PhysicalLocation, blank=True, null=True)
    location_owner = models.CharField(u"Who is responsable for this", max_length=100, help_text=u"Just the name",
    blank=True, null=True)

    def __unicode__(self):
        return u"%s @ %s (%s)" % (self.station_name, self.physical_location, self.location_owner)

class Part(models.Model):
    part_type = models.ForeignKey(PartType, verbose_name=u"Part Type")
    part_brand = models.ForeignKey(Brand, verbose_name=u"Brand")
    part_spec = models.CharField(u"Specs", max_length=255, help_text=u"Specs can be more identifying traces, such as 1G,"
    "Sata, etc. for Hard Drives", blank=True, null=True)
    reference_url = models.URLField(u"Reference URL", help_text=u"A URL with info regarding the part, manufacturer one"
    " is prefered", blank=True, null=True)
    part_state = models.ForeignKey(PartState, verbose_name=u"State of this part", blank=True, null=True)
    part_location = models.ForeignKey(Station, verbose_name=u"Where is this?", help_text=u"Typically a workstation",
    blank=True, null=True)
    part_physical_identifier = models.CharField(u"Physical Identifier", max_length=100, help_text=u"The text on the"
    "label dude", blank=True, null=True)

    def __unicode__(self):
        return u"%s %s %s @ %s (%s)" % (self.part_type, self.part_brand, self.part_spec, self.part_location,
                                            self.part_state)
