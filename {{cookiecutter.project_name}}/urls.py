from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from resources import views as resource_views

from {{cookiecutter.project_name}} import views

router = routers.DefaultRouter()

router.register(r"base", resource_views.BaseViewSet)

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r'^$', views.myview),
    url(r"^api/", include(router.urls)),
]
