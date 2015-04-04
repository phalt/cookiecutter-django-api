from __future__ import unicode_literals

from rest_framework import serializers

from .models import (
    BaseModel
)


class BaseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BaseModel
        fields = (
            "text",
        )
