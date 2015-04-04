from __future__ import unicode_literals

from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)

    edited = models.DateTimeField(auto_now=True)


class BaseModel(DateTimeModel):
    """ A base models """

    def __unicode__(self):
        return self.text

    text = models.CharField(max_length=100)
