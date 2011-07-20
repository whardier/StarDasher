import datetime

from hashlib import sha256

from django.db import models

from django_extensions.db.fields import UUIDField

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

class TagHash(models.Model):
    hash = models.TextField() #list representation of sorted list of tag names.. enables sorting... slow sorting which may want to be cached

class Tag(models.Model):
    name = models.CharField(max_length=1024)
    hashs = models.ManyToManyField(TagHash)

class Event(models.Model):

    #Always store as UTC naive
    start = models.DateTimeField(null=True, blank=True, db_index=True) # Also seen as event time
    #Always store as UTC naive
    answer = models.DateTimeField(null=True, blank=True, db_index=True)
    #Always store as UTC naive
    end = models.DateTimeField(null=True, blank=True, db_index=True)

    event_type = models.CharField(default='CDR', max_length=45) #Default to CDR
    event_type_user_defined = models.CharField(max_length=45, null=True, blank=True)

    callerid_name = models.CharField(max_length=80)
    callerid_number = models.CharField(max_length=80)
    callerid_ani = models.CharField(max_length=80)
    callerid_rdnis = models.CharField(max_length=80)
    callerid_dnid = models.CharField(max_length=80)

    callerid_presentation_name = models.CharField(max_length=80)
    callerid_presentation_number = models.CharField(max_length=80)

    source = models.CharField(max_length=160, null=True, blank=True)
    destination = models.CharField(max_length=160, null=True, blank=True) #Also seen as extension for event data

    sequence = models.IntegerField(null=True, blank=True)

    context = models.CharField(max_length=80, null=True, blank=True)

    channel = models.CharField(max_length=240, null=True, blank=True) #Also seen as channname for event data
    channel_tech = models.SmallIntegerField(null=True, blank=True) #Index with channel
    channel_counter = models.IntegerField() #Index with channel

    channel_destination = models.CharField(max_length=240, null=True, blank=True)
    channel_destination_tech = models.SmallIntegerField(null=True, blank=True) #Index with channel_destionation
    channel_destination_counter = models.IntegerField() #Index with channel_destination

    application = models.CharField(max_length=80, null=True, blank=True)
    application_data = models.CharField(max_length=80, null=True, blank=True)

    duration = models.IntegerField()
    duration_billed = models.IntegerField()

    disposition = models.SmallIntegerField(default=1)

    ama_flags = models.IntegerField()

    account_code = models.CharField(max_length=20, null=True, blank=True)
    account_code_peer = models.CharField(max_length=20, null=True, blank=True)

    user_field = models.CharField(max_length=256, null=True, blank=True)

    unique_id = models.CharField(max_length=150, null=True, blank=True)
    linked_id = models.CharField(max_length=150, null=True, blank=True)

    peer = models.CharField(max_length=80, null=True, blank=True)

    origin_id = models.IntegerField(null=True, blank=True, db_index=True)
    origin_sync_key = models.CharField(max_length=1024, null=True, blank=True)

    batch = models.ForeignKey(Batch)    
    tag_hash = models.ForeignKey(TagHash)

    custom_integer_01 = models.IntegerField(null=True, blank=True)
    custom_integer_02 = models.IntegerField(null=True, blank=True)
    custom_integer_03 = models.IntegerField(null=True, blank=True)
    custom_integer_04 = models.IntegerField(null=True, blank=True)
    custom_integer_05 = models.IntegerField(null=True, blank=True)
    custom_integer_06 = models.IntegerField(null=True, blank=True)
    custom_integer_07 = models.IntegerField(null=True, blank=True)
    custom_integer_08 = models.IntegerField(null=True, blank=True)
    custom_integer_09 = models.IntegerField(null=True, blank=True)
    custom_integer_10 = models.IntegerField(null=True, blank=True)
    custom_integer_11 = models.IntegerField(null=True, blank=True)
    custom_integer_12 = models.IntegerField(null=True, blank=True)
    custom_integer_13 = models.IntegerField(null=True, blank=True)
    custom_integer_14 = models.IntegerField(null=True, blank=True)
    custom_integer_15 = models.IntegerField(null=True, blank=True)
    custom_integer_16 = models.IntegerField(null=True, blank=True)
    custom_integer_17 = models.IntegerField(null=True, blank=True)
    custom_integer_18 = models.IntegerField(null=True, blank=True)
    custom_integer_19 = models.IntegerField(null=True, blank=True)
    custom_integer_20 = models.IntegerField(null=True, blank=True)

    custom_string_01 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_02 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_03 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_04 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_05 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_06 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_07 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_08 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_09 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_10 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_11 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_12 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_13 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_14 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_15 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_16 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_17 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_18 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_19 = models.CharField(max_length=1024, null=True, blank=True)
    custom_string_20 = models.CharField(max_length=1024, null=True, blank=True)

