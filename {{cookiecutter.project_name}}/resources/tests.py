from __future__ import unicode_literals

from django.test import TestCase

from .models import (
    BaseModel
)

class TestAllEndpoints(TestCase):
    """ Test ALL the endpoints """
    fixtures = [
    ]

    def get_query(self, url):
        return self.client.get(url)
