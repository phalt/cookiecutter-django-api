# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    """ A base models """

    def __unicode__(self):
        return self.text

    text = models.CharField(max_length=100)
