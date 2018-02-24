from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepage',
        'USER': 'homepage'
    }
}
