# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
