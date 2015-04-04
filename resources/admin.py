from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    BaseModel

)

classes = [BaseModel]

for c in classes:
    admin.site.register(c)
