# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response


def index(request):

    return render_to_response('base.html', {})
