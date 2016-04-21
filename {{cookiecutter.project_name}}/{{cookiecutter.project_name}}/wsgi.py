"""
WSGI config for {{cookiecutter.project_name}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from django.core.cache.backends.memcached import BaseMemcachedCache

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_name}}.settings")

# Fix django closing connection to MemCachier after every request (#11331)

BaseMemcachedCache.close = lambda self, **kwargs: None

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
