from __future__ import unicode_literals

from django.conf import settings

from rest_framework import viewsets

from .models import (
    BaseModel
)

from .serializers import (
    BaseSerializer
)

class BaseViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = BaseModel.objects.all()
    serializer_class = BaseSerializer
