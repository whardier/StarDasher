import datetime

from django.db import models

from django_extensions.db.fields import UUIDField

class CallerID(models.Model):
    name = models.CharField(max_length=80)
    number = models.CharField(max_length=80)
    ani = models.CharField(max_length=80)
    rdnis = models.CharField(max_length=80)
    dnid = models.CharField(max_length=80)
    presentation_name = models.CharField(max_length=80)
    presentation_number = models.CharField(max_length=80)
    #parent information can be retrieved through linkedid in Call

### TODO: Add indexes later after query analysis
class Batch(models.Model):
    UUID = UUIDField()
    #Always store as UTC naive
    created = models.DateTimeField(default=datetime.datetime.now())
    #Always store as UTC naive
    start = models.DateTimeField(null=True, blank=True)
    #Always store as UTC naive
    end = models.DateTimeField(null=True, blank=True)

    completed = models.BooleanField(default=0)

class TagGroup(models.Model):
    name = models.CharField(max_length=80) #Later used to deal with promotion codes and arbitrary data tagging.

class Tag(models.Model):
    name = models.CharField(max_length=80)
    group = models.ManyToManyField(TagGroup)

class TagHash(models.Model):
    hash = models.CharField(max_length=8192, db_index=1) #list representation of sorted list of tag names.. allows sorting.
    groups = models.ManyToManyField(TagGroup)

class CallDetailEvent(models.Model):

    #Always store as UTC naive
    start = models.DateTimeField(null=True, blank=True, db_index=True) # Also seen as event time
    #Always store as UTC naive
    answer = models.DateTimeField(null=True, blank=True, db_index=True)
    #Always store as UTC naive
    end = models.DateTimeField(null=True, blank=True, db_index=True)

    event_type = models.CharField(default='CDR', max_length=45) #Default to CDR
    event_type_user_defined = models.CharField(max_length=45, null=True, blank=True)

    callerid = models.ForeignKey(CallerID)

    source = models.CharField(max_length=160, null=True, blank=True)
    destination = models.CharField(max_length=160, null=True, blank=True) #Also seen as extension for event data

    context = models.CharField(max_length=80, null=True, blank=True)

    channel = models.CharField(max_length=240, null=True, blank=True) #Also seen as channname for event data
    channel_tech = models.SmallIntegerField(null=True, blank=True)
    channel_counter = models.IntegerField() #Index with channel

    channel_destination = models.CharField(max_length=240, null=True, blank=True)
    channel_destination_tech = models.SmallIntegerField(null=True, blank=True)
    channel_destination_counter = models.IntegerField() #Index with channel_destination

    application = models.CharField(max_length=80, null=True, blank=True)
    application_data = models.CharField(max_length=160, null=True, blank=True)

    duration_call = models.IntegerField()
    duration_billed = models.IntegerField()

    disposition = models.CharField(max_length=45, null=True, blank=True)

    ama_flags = models.IntegerField()

    account_code = models.CharField(max_length=160, null=True, blank=True)
    account_code_peer = models.CharField(max_length=160, null=True, blank=True)

    user_field = models.CharField(max_length=255, null=True, blank=True)

    unique_id = models.CharField(max_length=255, null=True, blank=True)
    linked_id = models.CharField(max_length=255, null=True, blank=True)

    peer = models.CharField(max_length=80, null=True, blank=True)

    origin_id = models.IntegerField(null=True, blank=True, db_index=True)
    origin_sync_key = models.CharField(max_length=255, null=True, blank=True)

    batch = models.ForeignKey(Batch)    
    tag_hash = models.ForeignKey(TagHash)
