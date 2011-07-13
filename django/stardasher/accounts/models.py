from django.conf import settings
from django.db import models

from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

from django.db.models.signals import post_save

import pytz

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    timezone = models.CharField('Timezone Preference', max_length=50, choices=[(x,x) for x in sorted(pytz.all_timezones)])

    date_created = CreationDateTimeField(db_index=True)
    date_modified = ModificationDateTimeField(db_index=True)

    def __unicode__(self):
        return unicode(self.user)

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = UserProfile()
        profile.user = user
        profile.save()
    else:
        try:
            user.get_profile().save()
        except:
            pass

post_save.connect(create_profile, sender=User)

class Account(models.Model):
    name = models.CharField(_('name'), max_length = 50, db_index=True)

    date_created = CreationDateTimeField(db_index=True)
    date_modified = ModificationDateTimeField(db_index=True)

    groups = models.ManyToManyField(Group, null=True, blank=True)

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def __unicode__(self):
        return self.name

