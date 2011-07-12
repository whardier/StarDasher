import datetime

from django.db import models

from django_extensions.db.fields import UUIDField

### TODO: Add indexes later after query analysis

class String45(models.Model):
    value = models.CharField(max_length=45)
    preload = models.BooleanField(default=False) #Checked occasionally and on server startup through delayed events

class String80(models.Model):
    value = models.CharField(max_length=80)
    preload = models.BooleanField(default=False)

class String160(models.Model):
    value = models.CharField(max_length=160)
    preload = models.BooleanField(default=False)

class String240(models.Model):
    value = models.CharField(max_length=240)
    preload = models.BooleanField(default=False)

class String255(models.Model):
    value = models.CharField(max_length=255)
    preload = models.BooleanField(default=False)

class CallerID(models.Model):
    name = models.CharField(max_length=80)
    number = models.CharField(max_length=80)
    ani = models.CharField(max_length=80)
    rdnis = models.CharField(max_length=80)
    dnid = models.CharField(max_length=80)
    presentation_name = models.CharField(max_length=80)
    presentation_number = models.CharField(max_length=80)
    #parent information can be retrieved through linkedid in Call

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
    hash = models.CharField(max_length=64, db_index=1) #sha256 sum of sorted list representation of all tags concatenated with groups ['tag:group', '...']
    groups = models.ManyToManyField(TagGroup)

class CallDetailEvent(models.Model):

    #Always store as UTC naive
    start = models.DateTimeField(null=True, blank=True) # Also seen as event time
    #Always store as UTC naive
    answer = models.DateTimeField(null=True, blank=True)
    #Always store as UTC naive
    end = models.DateTimeField(null=True, blank=True)

    type_event = models.ForeignKey(String45, related_name='type_event') #Default to CDR
    type_user_defined = models.ForeignKey(String45, null=True, blank=True, related_name='type_user_defined')

    callerid = models.ForeignKey(CallerID)

    source = models.ForeignKey(String160, null=True, blank=True, related_name='source')
    destination = models.ForeignKey(String160, null=True, blank=True, related_name='destination') #Also seen as extension for event data

    context = models.ForeignKey(String80, null=True, blank=True, related_name='context')

    channel = models.ForeignKey(String240, null=True, blank=True, related_name='channel') #Also seen as channname for event data
    channel_tech = models.ForeignKey(String45, null=True, blank=True, related_name='channel_tech')
    channel_counter = models.IntegerField() #Index with channel
    channel_destination = models.ForeignKey(String240, null=True, blank=True, related_name='channel_destination')
    channel_destination_tech = models.ForeignKey(String45, null=True, blank=True, related_name='channel_destination_tech')
    channel_destination_counter = models.IntegerField() #Index with channel_destination

    application = models.ForeignKey(String80, null=True, blank=True, related_name='application')
    application_data = models.ForeignKey(String160, null=True, blank=True, related_name='application_data')

    duration_call = models.IntegerField()
    duration_billed = models.IntegerField()

    disposition = models.ForeignKey(String45, null=True, blank=True, related_name='disposition')

    ama_flags = models.IntegerField()

    account_code = models.ForeignKey(String160, null=True, blank=True, related_name='account_code')
    account_code_peer = models.ForeignKey(String160, null=True, blank=True, related_name='account_code_peer')

    user_field = models.ForeignKey(String255, null=True, blank=True, related_name='userfield')

    unique_id = models.ForeignKey(String255, null=True, blank=True, related_name='unique_id')
    linked_id = models.ForeignKey(String255, null=True, blank=True, related_name='linked_id')

    peer = models.ForeignKey(String80, null=True, blank=True, related_name='peer')

    batch = models.ForeignKey(Batch)
    
    tag_hash = models.ForeignKey(TagHash)

