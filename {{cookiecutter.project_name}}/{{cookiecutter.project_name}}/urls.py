# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import routers

from resources import views as resource_views

from {{cookiecutter.project_name}} import views

from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()

router.register(r"base", resource_views.BaseViewSet)

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r'^$', views.index),
    url(r"^api/", include(router.urls)),
]
