# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
